#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/27 13:07
# @Author: 白云苍狗
# @File: 01- 高阶函数.py
# @Software: PyCharm

"""
1- 高阶函数: 接受函数为参数，或者把函数作为结果返回的函数是高阶函数。
     例如，内置函数map()、filter()和reduce()就是高阶函数，因为它们的第一个参数是函数。

"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# 任何单参数函数都能作为key参数的值。
fruits = sorted(fruits, key=len)
print(fruits)  # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# map高阶函数
print(list(map(factorial, range(6))))  # [1, 1, 2, 6, 24, 120]
print([factorial(n) for n in range(6)])  # [1, 1, 2, 6, 24, 120]
# map和filter返回生成器，因此现在它们的直接替代品是生成器表达式。
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # [1, 6, 120]
print([factorial(n) for n in range(6) if n % 2])  # [1, 6, 120]
