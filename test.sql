create TABLE test_all(
业务区域 varchar(64),
业务区域编码 varchar(32),
门店 varchar(128),
门店编码 varchar(32),
员工编号 varchar(64) primary key,
姓名 varchar(32),
身份证号 varchar(128),
手机号码 varchar(64),
性别 enum('male','female'),
年龄 varchar(16),
入职日期 varchar(64),
离职日期 varchar(64),
复职日期 varchar(64),
职务 varchar(32),
最高教育程度 varchar(64),
学历证书编号 varchar(128),
毕业年份 varchar(32),
毕业院校 varchar(128),
所学专业 varchar(128),
紧急联系人姓名 varchar(32),
紧急联系人电话 varchar(32),
状态 varchar(16)
)

CREATE TABLE atest(
    姓名 varchar(64) PRIMARY KEY,
    年龄 varchar(32),
    性别 enum('male','female')
)