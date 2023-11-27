#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/9 19:30
# @Author: 白云苍狗
# @File: 冒泡排序.py
# @Software: PyCharm


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sort(alist))
