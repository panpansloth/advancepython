#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:37
# @Author: 白云苍狗
# @File: 04- set和frozenset.py
# @Software: PyCharm
"""
1- set和frozenset都是可以用于存储唯一元素的集合类型。
2- 主要区别在于set是可变的，而frozenset是不可变的。
"""
s = {1, 2, 3}
print(s)  # {1, 2, 3}
s.remove(1)
print(s)  # {2, 3}

fs = frozenset({1, 2, 3})
print(fs)  # frozenset({1, 2, 3})
d = {fs: 'frozenset'}
print(d)  # {frozenset({1, 2, 3}): 'frozenset'}
try:
    fs.add(4)
except AttributeError as e:
    print(e)  # 'frozenset' object has no attribute 'add'
