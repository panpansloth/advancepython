#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:14
# @Author: 白云苍狗
# @File: 1. 连接数据库.py
# @Software: PyCharm


# 1. 导入pymysql模块
import pymysql

# 2. 获取连接
connection = pymysql.connect(host='localhost', user='root', password='panpan', db='myemployees', charset='utf8')
# 3. 创建cursor
cursor = connection.cursor()
# 4. 编写sql语句
sql = 'select * from employees'
# 5. 执行sql语句
cursor.execute(sql)
# 6. 查看结果集
employees = cursor.fetchall()
for employee in employees:
    print(employee)
