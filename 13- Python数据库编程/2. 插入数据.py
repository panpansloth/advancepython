#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:22
# @Author: 白云苍狗
# @File: 2. 插入数据.py
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
sql = 'insert into employees values(99, "白云", "苍狗", "peiyaol.sloth@outlook.com", "12345678901", "IT_PROG", 100000, NULL, NULL, 90)'
try:
    # 4. 执行sql语句
    cursor.execute(sql)
    # 5. 提交事务
    connection.commit()
except:
    # 5. 回滚事务
    connection.rollback()
finally:
    # 6. 关闭connection
    connection.close()
