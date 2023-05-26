#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:41
# @Author: 白云苍狗
# @File: 02- __getattr__和__getattribute__魔术方法.py
# @Software: PyCharm

"""
__getattr__、__getattribute__魔术方法：
1- __getattr__：在查找不到属性的时候调用
2- __getattribute__：在查找属性的时候调用

"""


class User:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        return f'Not found attribute {item}'


class User1:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        # 只要调用属性，就会出发__getattribute__方法
        return '神奇的代理操作'


if __name__ == '__main__':
    user = User('白云苍狗')
    print(user.name)  # 白云苍狗
    print(user.age)  # Not found attribute age

    user1 = User1('白云苍狗')  # 神奇的代理操作
    print(user1.name)
