# 创建一个库spider ，创建表t1，插入1条记录。。。
import pymysql

# 1，创建数据库连接对象
db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
# 2，创建游标对象
cursor = db.cursor()
# 3，执行语句
cursor.execute("create database if not exists spiderdb00 character set utf8")
cursor.execute("use spiderdb00")
cursor.execute("create table in not exists t1(id int,name varchar(20))")
ins = "insert into t1 values(%s,%s)"
cursor.execute(ins, [1, "yangs"])
# cursor.execute(ins,[2])
# 4，提交
db.commit()
# 5，关闭
cursor.close()
db.close()
