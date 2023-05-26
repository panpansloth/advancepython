#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 14:25
# @Author: 白云苍狗
# @File: 05- nonlocal声明.py
# @Software: PyCharm

"""
1- nonlocal声明的作用
    1. 是把变量标记为自由变量，即使在函数中为变量赋予新值了。
    2. 如果为nonlocal声明的变量赋予新值，闭包中保存的绑定会更新。
"""

"""
def make_averager():
    '''计算累计平均值的高阶函数，不保存所有历史值，但是有缺陷'''
    count = 0
    total = 0

    def averager(new_value):
        # 我们在averager的主体中为count赋值了，这会把count变成局部变量。total变量也受着这个问题影响。
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
avg(10)  # UnboundLocalError: local variable 'count' referenced before assignment
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))  # 10.0
    print(avg(11))  # 10.5
    print(avg(12))  # 11.0
