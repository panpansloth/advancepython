#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/9 19:51
# @Author: 白云苍狗
# @File: 归并排序.py
# @Software: PyCharm
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(alist, left_half, right_half)
    return alist


def merge(alist, left_half, right_half):
    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            alist[k] = left_half[i]
            i += 1
        else:
            alist[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        alist[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        alist[k] = right_half[j]
        j += 1
        k += 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist = merge_sort(alist)
print(alist)
