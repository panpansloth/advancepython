#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/12 20:51
# @Author: 白云苍狗
# @File: 06- __slots__作用.py
# @Software: PyCharm

"""
__slots__作用：
1- 对动态添加成员变量、成员方法有限制。
2- 对动态添加类属性和类方法没有限制。
3- 只对本类有限制，不限制子类。
"""


class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    Person.gender = 'man'
    print(Person.gender)  # man

    person = Person('白云苍狗', 29)
    # person.gender = 'man'  # AttributeError: 'Person' object has no attribute 'gender'
