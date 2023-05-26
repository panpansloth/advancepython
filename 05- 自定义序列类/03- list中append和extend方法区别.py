#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/4 17:08
# @Author: 白云苍狗
# @File: 03- list中append和extend方法区别.py
# @Software: PyCharm
"""
list中append和extend方法区别：
1- append方法是将一个对象添加到列表中。
2- extend方法是将一个列表添加到另一个列表中。
"""
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)  # [1, 2, 3, [4, 5, 6]]
a.extend(b)
print(a)  # [1, 2, 3, [4, 5, 6], 4, 5, 6]
