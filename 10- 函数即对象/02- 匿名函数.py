#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 14:30
# @Author: 白云苍狗
# @File: 02- 匿名函数.py
# @Software: PyCharm
"""
匿名函数： lambda关键字在Python表达式创建匿名函数。
    1. 在高阶函数的参数列表中最适合使用匿名函数。
    2. 除了作为参数传递给高阶函数之外，Python很少使用匿名函数。
"""
# 匿名函数的例子
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
