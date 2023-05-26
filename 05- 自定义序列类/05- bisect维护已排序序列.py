#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/4 17:09
# @Author: 白云苍狗
# @File: 05- bisect维护已排序序列.py
# @Software: PyCharm
"""

"""
import bisect

my_list = []
bisect.insort(my_list, 5)
bisect.insort(my_list, 2)
bisect.insort(my_list, 7)
bisect.insort(my_list, 1)
bisect.insort(my_list, 9)
bisect.insort(my_list, 3)


print(my_list)  # [1, 2, 3, 5, 7, 9]

print(bisect.bisect(my_list, 4))  # 3
