#写各种数据处理函数
import pymysql
dbconn = pymysql.connect('127.0.0.1','root','123456','test',charset='utf8')
cursor = dbconn.cursor()
def regist(name,age,gender):
    sql = '''insert into atest
    values('%s','%s','%s')'''%(name,age,gender)
    try:
        cursor.execute(sql)
        dbconn.commit()
        return True
    except Exception as e:
        return e
        



def login(info):
    pass




import time

def show_time():
    return time.ctime()

def say_hello():
    return "Hello Python"

def say_bye():
    return "Bye everyone" 

