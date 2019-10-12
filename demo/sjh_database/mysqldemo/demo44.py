# -*- encoding: utf-8 -*-
import mysql.connector

mysql_conf = {'host': '127.0.0.1', 'database': 'python', 'port': 3306,
              'user': 'root', 'password': 'root',
              'use_unicode': True,
              'raise_on_warnings': True}
conn = mysql.connector.connect(**mysql_conf)
cursor = conn.cursor()
sql_insert = ("insert into person (name,age) values(%s,%s) ")
sql_insert_data = ('zhangsan', 18)
cursor.execute(sql_insert, sql_insert_data)
conn.commit()
cursor.close()
conn.close()
