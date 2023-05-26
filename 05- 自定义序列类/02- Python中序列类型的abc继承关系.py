#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/4 17:08
# @Author: 白云苍狗
# @File: 02- Python中序列类型的abc继承关系.py
# @Software: PyCharm
"""
Python是基于协议的语言，结合鸭子类型和魔法函数，就可以实现某种类型。
不同魔法函数的组合，构建不同的类型。
Iterable: __iter__
Reversible: __reversed__
Sized: __len__
Container: __contains__
Collection: Size, Iterable, Container
Sequence: __getitem__, Reversible, Collection
MutableSequence: __setitem__, __delitem__, Sequence
"""

from collections.abc import *


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

    def __getitem__(self, item):
        pass

    # def __iter__(self):
    #     pass


if __name__ == '__main__':
    company = Company(['panda', 'dog'])

    print(hasattr(company, '__len__'))  # True
    print(isinstance(company, Sized))  # True
    print(isinstance(company, Iterable))  # True
