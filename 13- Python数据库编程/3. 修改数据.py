#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:34
# @Author: 白云苍狗
# @File: 3. 修改数据.py
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
sql = 'update employees set salary = 1000000 where employee_id = 99'
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
