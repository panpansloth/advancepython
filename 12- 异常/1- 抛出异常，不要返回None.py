#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 15:53
# @Author: 白云苍狗
# @File: 1- 抛出异常，不要返回None.py
# @Software: PyCharm

"""
用异常来表示错误情况，而不是返回None
"""


def careful_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


if __name__ == '__main__':
    x, y = 0, 0
    try:
        result = careful_divide(x, y)
    except ValueError:
        print('Invalid inputs')
    else:
        print('Result is %.1f' % result)
