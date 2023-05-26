#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/22 0:24
# @Author: 白云苍狗
# @File: 05- 类属性和实例属性的查找顺序.py
# @Software: PyCharm

"""
当实例对象a访问name属性时，先在实例对象a中查找name属性:
    a- 找到了，就返回实例对象a中的name属性。
    b- 没有找到，再去类A中查找:
        1- 找到了，就返回类A中的name属性。
        2- 类A中也没有name属性，就会报错。
"""
class A:
    name = 'A'

    def __init__(self):
        self.name = 'obj'

a = A()
print(a.name)  # obj


