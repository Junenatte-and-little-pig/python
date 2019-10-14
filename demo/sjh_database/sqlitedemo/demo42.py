# -*- encoding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("sqlitedemo.db")
try:
    # 游标对象进行增删改查操作
    cursor = conn.cursor()
    sql_select = ("select id,name,age,salary from user")
    result = cursor.execute(sql_select)
    print(result.fetchall())
    # 操作结束后要通过连接对象进行提交
    conn.commit()
except Exception as e:
    print(repr(e))
finally:
    conn.close()
