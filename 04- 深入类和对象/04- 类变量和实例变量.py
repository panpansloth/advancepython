#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/22 0:04
# @Author: 白云苍狗
# @File: 04- 类变量和实例变量.py
# @Software: PyCharm
"""
https://docs.python.org/zh-cn/3/tutorial/classes.html#class-and-instance-variables

1- 类变量和实例变量的相同点
    类变量和实例变量都可以通过类的实例化对象来访问。
    类变量和实例变量都可以通过类的实例化对象来修改。

2- 类变量和实例变量的区别
    类变量
    1. 类变量用于类的所有实例共享的属性和方法
    2. 既可以使用类名直接调用，也可以使用实例对象调用

    实例变量
    1. 实例化之后，每个实例单独拥有的变量
    2. 实例变量在类内部用 self 访问，在类外部用实例对象访问
    3. `__dict__`：对象的属性，用于存储自身实例变量的字典
"""


class Dog:
    # class variable shared by all instances
    kind = 'canine'

    def __init__(self, name):
        # instance variable unique to each instance
        self.name = name


# 实例化对象
a = Dog('Fido')
b = Dog('Buddy')

# 不能通过类名访问实例变量
# print(Dog.name)  # AttributeError: type object 'Dog' has no attribute 'name'

# 为实例a动态增加属性kind
a.kind = 'panda'

# 修改类变量
Dog.kind = 'sloth'
print(a.kind, b.kind, Dog.kind)  # panda sloth sloth

