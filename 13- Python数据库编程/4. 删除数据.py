#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:37
# @Author: 白云苍狗
# @File: 4. 删除数据.py
# @Software: PyCharm
import pymysql

db_info = {
    'host': 'localhost',
    'user': 'root',
    'password': 'panpan',
    'db': 'myemployees',
    'charset': 'utf8'
}
# 1. 获取连接
connection = pymysql.connect(**db_info)
# 2. 创建cursor
cursor = connection.cursor()
# 3. 编写sql语句
sql = 'delete from employees where employee_id = 99'
try:
    # 4. 执行sql
    cursor.execute(sql)
    connection.commit()
except:
    # 5. 回滚事务
    connection.rollback()
finally:
    # 6. 关闭connection
    connection.close()
