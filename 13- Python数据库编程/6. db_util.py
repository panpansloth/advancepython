#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 10:51
# @Author: 白云苍狗
# @File: 6. db_util.py
# @Software: PyCharm
"""
上下文管理器协议包含__enter__和__exit__两个方法。
1- with语句开始运行时，会在上下文管理器对象上调用__enter__方法。
2- with语句运行结束时，会在上下文管理器对象上调用__exit__方法，以此扮演finally的角色。


"""
import pymysql


class DBUtil:
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'panpan',
        'db': 'myemployees',
        'charset': 'utf8'
    }

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self.config)
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise e
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def query_one(self, sql, *args):
        # 查询单条数据
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)

    def query_all(self, sql, *args):
        # 查询全部数据
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def execute_dml(self, sql, *args):
        # 执行增删改操作
        try:
            self.cursor.execute(sql, args)
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()


if __name__ == '__main__':
    with DBUtil() as db_util:
        sql2 = 'insert into employees(employee_id, first_name, last_name) values(%s,%s,%s)'
        db_util.execute_dml(sql2, 98, '白云', '苍狗')

        sql = 'select * from employees where employee_id = %s'
        result = db_util.query_one(sql, 98)
        print(result)

        sql1 = 'delete from employees where employee_id = %s'
        db_util.execute_dml(sql1, 98)

        sql3 = 'select * from employees'
        result3 = db_util.query_all(sql3)
        print(result3)
