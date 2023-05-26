#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/21 17:52
# @Author: 白云苍狗
# @File: all_is_object.py
# @Software: PyCharm
"""
Python中一切皆对象(函数和类都是对象)
1. 赋值给一个变量
2. 可以添加到集合对象中
3. 可以作为参数传递给函数
4. 可以当作函数的返回值
"""
def ask(name='panda'):
    print(name)

my_func = ask
my_func()

class Person:
    def __init__(self):
        print('panda')
my_class = Person
my_class()

obj_list = [ask, Person]
for item in obj_list:
    print(item())

def decorator_func():
    print('decorator_func')
    return ask
my_ask = decorator_func()
my_ask('dog')