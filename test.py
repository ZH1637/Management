#coding=utf-8
'''
模拟网站后端处理程序
'''
from socket import *
from select import * 
import sys
import pymysql
from settings import *
import xlrd,xlwt

# fr = xlrd.open_workbook(r'12月结账运营人力数据_20190102_V1116.xlsx')
# table = fr.sheet_by_name('在职')
# row = table.row(0)
# print(row)


# if len(sys.argv) < 3:
#     pass
# else:
#     frame_ip = sys.argv[1]
#     frame_port = int(sys.argv[2])
frame_address = (frame_ip,frame_port)
db_conn = None
def conn_database():
    global db_conn
    db_conn = pymysql.connect(mysql_host,mysql_user,mysql_pwd,dbname)
    if not db_conn:
        print('连接数据库失败')
        return -1
    else:
        return 0


#应用类，将功能封装
class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(frame_address)
        self.rlist = [self.sockfd]
        self.wlist = []
        self.xlist = []
    
    def runserver(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%frame_port)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    request = r.recv(1024).decode()
                    self.handle(r,request)
    
    def handle(self,connfd,request):
        method = request.split(' ')[0]
        path_info = request.split(' ')[1]

        if method == 'GET':
            if path_info=='/' or path_info[-5:]=='.html':
                response = self.get_html(path_info)
            else:
                response = self.get_data(path_info)
        elif method == 'POST':
            pass
        connfd.send(response.encode())
        connfd.close()
        self.rlist.remove(connfd)
    
    def get_html(self,path_info):
        if path_info == "/":
            get_file = STATIC_DIR + "/index.html"
        else:
            get_file = STATIC_DIR + path_info
        try:
            fd = open(get_file)
        except IOError:
            response = "404"
        else:
            response = fd.read()
        finally:
            return response
    
    def get_data(self,path_info):
        for url,func in urls:
            if path_info == url:
                response = func()
                break
        else:
            response = '404'
        return response
        

if __name__ == "__main__":
    app = Application()
    app.runserver() #启动应用框架服务
