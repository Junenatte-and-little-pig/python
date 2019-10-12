# -*- encoding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("sqlite.db")
try:
    sql_create_table = ("create table if not exists user"
                        "("
                        "id integer not null primary key autoincrement,"
                        "name text,"
                        "age integer,"
                        "salary real"
                        ")")
    conn.execute(sql_create_table)

    # 游标对象进行增删改查操作
    cursor = conn.cursor()
    sql_insert = ("insert into user(name,age,salary)"
                  "values('zhangsan',18,5000)"
                  )
    cursor.execute(sql_insert)
    # 操作结束后要通过连接对象进行提交
    conn.commit()
except Exception as e:
    print(repr(e))
    conn.rollback()
finally:
    conn.close()
