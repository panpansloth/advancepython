#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/8 18:13
# @Author: 白云苍狗
# @File: 01- 可迭代对象和迭代器.py
# @Software: PyCharm
"""
1- Iterable：使用内置函数iter可以获取迭代器的对象。
    1. 如果对象实现了能返回迭代器的__iter__方法，那么对象就是就是可迭代的。
    2. 序列类型（如list、str、tuple）都可以迭代。实现了__getitem__方法，而且其参数是从0开始的索引，这种对象也可以迭代。

2- Iterator：迭代器是实现了迭代器协议的对象。Python标准的迭代器接口有两个方法：__iter__()和__next__()。
    1. __iter__()：返回self，以便在预期可迭代对象的地方使用迭代器，例如for循环中。
    def __iter__(self):
        return self
    2. __next__()：返回序列中的下一项，如果没有下一项了，就抛出StopIteration异常。

3- 可迭代对象和迭代器的关系：Python从可迭代对象中获取迭代器。

"""
