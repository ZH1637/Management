import pymysql
host = 'localhost'
user = 'root'
password = '123456'
dbname = 'STU_INFO'
conn = pymysql.connect(host,user,password,dbname,charset='utf8')

cursor = conn.cursor()

class Student:
    global cursor
    # 添加学生信息
    def input(self):
        while True:
            try:
                name = input('请输入姓名:')
                if not name:
                    break
                age = int(input('请输入年龄:'))
                score = int(input('请输入成绩:'))
                if age not in range(1,101):
                    raise TypeError
                if score not in range(0,101):
                    raise TypeError
                sql = '''insert into info values(
                    '%s',%d,%d
                )
                '''%(name,age,score)
                cursor.execute(sql)
                conn.commit()
            except TypeError:
                print('输入不合法请重新输入!')
            except Exception as e:
                print(e)
            else:    
                print('添加成功!')


    # 显示学生信息
    def out(self):
        pass
    # 删除学生信息
    def delete(self):
        pass
    # 修改学生信息
    def change(self):
        pass
    # 按学生成绩高~低显示学生信息
    def score_down(slef):
        pass
    # 按学生成绩低~高显示学生信息
    def score_up(self):
        pass
    # 按学生年龄高~低显示学生信息
    def age_down(self):
        pass
    # 按学生年龄低~高显示学生信息
    def age_up(self):
        pass
    # 保存信息到文件(info.txt)
    def save(self):
        pass

s = Student()
s.input()