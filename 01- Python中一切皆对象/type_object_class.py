#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/21 18:03
# @Author: 白云苍狗
# @File: type_object_class.py
# @Software: PyCharm
"""
1. type是一切type的类型
2. object是所有对象的基类，type也继承自object
3. object的type是type
"""
# 1. type是一切type的类型
print(type('panda'))  # <class 'str'>
print(type(str))  # <class 'type'>

# 2. object是所有对象的基类，type也继承自object
print(type.__bases__)  # (<class 'object'>,)

# 3. object的type是type
print(type(object))  # <class 'type'>
