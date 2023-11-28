#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/27 19:25
# @Author: 白云苍狗
# @File: handler_mysql.py
# @Software: PyCharm

"""
MySQLDatabase类现在实现了上下文管理器的方法：__enter__和__exit__。
这种方式确保了即使在发生异常的情况下，数据库连接也能被安全地关闭。

with MySQLDatabase(config) as db:语句，
1- __enter__方法自动调用connect方法来建立数据库连接，返回的db对象可以用于执行查询或修改。
2- 离开with块时，__exit__方法自动调用close方法来关闭数据库连接。
"""
import pymysql


class MySQLDatabase:
    def __init__(self, config):
        """
        Initialize the database connection using a configuration dictionary.
        The dictionary should contain keys for 'host', 'user', 'password', 'database', and optionally 'port'.
        """
        self.config = config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        """Establish a connection to the database using the provided configuration."""
        try:
            self.connection = pymysql.connect(**self.config, cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()
            print("Connection to MySQL database successful")
        except Exception as e:
            print(f"Error connecting to MySQL database: {e}")

    def execute_query(self, query):
        """Execute a SELECT query and return the results."""
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def execute_modification(self, sql):
        """Execute a modification (INSERT, UPDATE, DELETE) SQL statement."""
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("SQL modification executed successfully")
        except Exception as e:
            self.connection.rollback()
            print(f"Error executing modification: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("MySQL database connection closed")


if __name__ == '__main__':
    # 数据库配置文件
    _config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'panpan',
        'database': 'smallrelationsinsertfile',
        'port': 3306  # optional, default is 3306
    }

    with MySQLDatabase(_config) as db:
        # Execute an UPDATE/INSERT/DELETE query
        db.execute_modification('UPDATE instructor SET salary = 65000 WHERE ID = 10101')

        # Execute a SELECT query
        results = db.execute_query('SELECT * FROM instructor')
        print(results[0])
