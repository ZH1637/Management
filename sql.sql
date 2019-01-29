create table user(
用户名 varchar(32) not null,
密码   varchar(128) not null
);

insert into user values
('zhang',123456),
('san',654321),
('li',111111),
('si',222222);

select * from user
where 用户名 = 'zhang'
and 密码 = '123456';

create table info(
    name varchar(32) PRIMARY KEY,
    age int,
    score int
);

insert into info values