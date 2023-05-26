#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:40
# @Author: 白云苍狗
# @File: 01- @property.py
# @Software: PyCharm

"""
@property：用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值。

"""
from datetime import date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return date.today().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

    def get_age(self):
        return self._age


if __name__ == '__main__':
    user = User('linda', date(1993, 11, 8))
    print(user.age)  # 30
    user.age = 29
    print(user.get_age())  # 29
