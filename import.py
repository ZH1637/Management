import pymysql
import xlrd,xlwt




dbconn = pymysql.connect('localhost','root','123456','test',charset='utf8')
cursor = dbconn.cursor()
fr = xlrd.open_workbook(r'12月结账运营人力数据_20190102_V1116.xlsx')
table = fr.sheet_by_name('详细信息')
for i in range(1,table.nrows):
    row = table.row(i)
    line = []
    for x in row:
        value = str(x).split(':')[1]
        line.append(value)
    sql = '''insert into test_all values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''%(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],
    line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],
    line[19],line[20],line[21])
    cursor.execute(sql)


dbconn.close()