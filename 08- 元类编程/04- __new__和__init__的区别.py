#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:42
# @Author: 白云苍狗
# @File: 04- __new__和__init__的区别.py
# @Software: PyCharm
"""
1- __new__和__init__的区别：
    1- __new__是一个静态方法，而__init__是一个实例方法。
    2- 当创建一个新实例时调用__new__，初始化一个实例时用__init__。
    3- __new__方法会返回一个创建的实例，而__init__什么都不返回。
    4- __new__方法在__init__之前调用。（只有在__new__返回一个cls的实例时，后面的__init__才能被调用。）
"""


class User:
    def __new__(cls, *args, **kwargs):
        print('调用__new__方法')
        return super().__new__(cls)

    def __init__(self, name):
        print('调用__init__方法')
        self.name = name


if __name__ == '__main__':
    user = User('白云苍狗')
    """
    调用__new__方法
    调用__init__方法
    """
