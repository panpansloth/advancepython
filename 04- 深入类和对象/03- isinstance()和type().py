#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/21 23:47
# @Author: 白云苍狗
# @File: 03- isinstance()和type().py
# @Software: PyCharm
"""
isinstance() 与 type() 区别：
1- type() 不会认为子类是一种父类类型，不考虑继承关系。
2- isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
"""
class A:
    pass

class B(A):
    pass
b = B()
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True
print(type(b) is B)  # True
print(type(b) is A)  # False