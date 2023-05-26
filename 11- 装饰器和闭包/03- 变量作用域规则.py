#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 17:27
# @Author: 白云苍狗
# @File: 03- 变量作用域规则.py
# @Software: PyCharm
"""
1- 变量作用域规则
    1. 模块全局作用域：在类或函数块外部分配值的名称。
    2. f3函数局部作用域：通过参数或者在函数内部分配值的名称。
    3. 变量还有可能出现在第3个作用域中，我们称之为"非局部"作用域。这个作用域是闭包的基础。

"""
b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == '__main__':
    f3(3)
    print(b)  # 9
