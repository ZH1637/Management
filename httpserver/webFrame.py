#coding=utf-8
'''
模拟网站后端处理程序
'''
from socket import *
from select import * 
import sys 
from views import *
import urllib
import urllib.parse
import urllib.request

frame_ip = "127.0.0.1"
frame_port = 8080
if len(sys.argv) < 3:
    pass
else:
    frame_ip = sys.argv[1]
    frame_port = int(sys.argv[2])
frame_address = (frame_ip,frame_port)

#静态网页位置
STATIC_DIR = './static'

#url列表，决定我们可以处理什么样的数据请求
urls = [
    ('/index',show_time),
    ("/hr",say_hello),
    ('/workers',say_bye)
]

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
                    request = r.recv(4096).decode()
                    # print(request.encode())
                    self.handle(r,request)
    
    def handle(self,connfd,request):
        request_lines = request.splitlines()
        # 获取请求行 login?name=张三&age=50&gender=male
        request_line=request_lines[0]
        method = request_line.split(' ')[0]
        path_info = request_line.split(' ')[1]
        

        if method == 'GET':
            if path_info=='/' or path_info[-5:]=='.html':
                response = self.get_html(path_info)
            elif '/login' in path_info:
                print(type(path_info))
                response = self.put_mysql(path_info.split('?')[1].split(' ')[0])
            else:
                response = self.get_data(path_info)
        elif method == 'POST':
            pass
            
        connfd.send(str(response).encode())
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
    
    def put_mysql(self,path_info):
        name = path_info.split('&')[0].split('=')[1]
        name = urllib.request.unquote(name)
        age = path_info.split('&')[1].split('=')[1]
        gender = path_info.split('&')[2].split('=')[1]
        res = regist(name,age,gender)
        if res==True:
            return True
        else:
            print(res)
            return False
        
        

    
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




# string = '%......'
# string = urllib.request.unquote(string)