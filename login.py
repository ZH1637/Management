import pymysql
host = 'localhost'
user = 'root'
password = '123456'
dbname = 'STU_INFO'
conn = pymysql.connect(host,user,password,dbname,charset='utf8')
def login():
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    sql = '''select * from user
    where 用户名 = '%s'
    and 密码 = %s
    '''%(user,passwd)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False



