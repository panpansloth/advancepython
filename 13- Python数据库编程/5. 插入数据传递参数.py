#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:44
# @Author: 白云苍狗
# @File: 5. 插入数据传递参数.py
# @Software: PyCharm
import pymysql

db_info = {
    'host': 'localhost',
    'user': 'root',
    'password': 'panpan',
    'db': 'myemployees',
    'charset': 'utf8'
}
connection = pymysql.connect(**db_info)
cursor = connection.cursor()
sql = 'insert into employees(employee_id,first_name,last_name) values(%s,%s,%s)'
try:
    cursor.execute(sql, (99, '白云', '苍狗'))
    connection.commit()
except:
    connection.rollback()
finally:
    connection.close()
