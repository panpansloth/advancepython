#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:39
# @Author: 白云苍狗
# @File: 02- ==和is的区别.py
# @Software: PyCharm

"""
1- 区别：
    1. ==运算符比较两个对象的值（对象存储的数据）；
    3. is比较对象的标识。
2- 比较一个变量和一个单例时，应该使用is。最常使用is检查变量绑定的值是不是None。
    x is None
    否定的正确写法：
    x is not None
3- 我们更关注对象的相等性，而不是同一性。
    1. 一般来说，is运算符只用于测试None。
    2. 如果不确定，那就使用==。
"""
