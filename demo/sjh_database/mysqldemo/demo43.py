# -*- encoding: utf-8 -*-
# AttributeError: module 'mysql.connector' has no attribute 'CMySQLConnection'
# from mysql.connector import *
import mysql.connector
mysql_conf = {'host': '127.0.0.1', 'database': 'python', 'port': 3306,
              'user': 'root', 'password': 'root',
              'use_unicode': True,
              'raise_on_warnings': True}
conn = mysql.connector.connect(**mysql_conf)
cursor=conn.cursor()
sql_create_table = ("create table if not exists person"
                       "("
                       "id integer not null primary key auto_increment,"
                       "name varchar(8),"
                       "age integer"
                       ")")
cursor.execute(sql_create_table)
