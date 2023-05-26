#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/21 18:51
# @Author: 白云苍狗
# @File: 02- 抽象基类(abc)模块.py
# @Software: PyCharm
from collections.abc import Sized


# 检查某个类是否有某个方法
# 1. hasattr
# 2. isinstance


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(['panda', 'dog'])

print(hasattr(company, '__len__'))  # True
print(isinstance(company, Sized))  # True
