#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/12 18:19
# @Author: 白云苍狗
# @File: 06- 统计传入的列表中每个数字出现的次数并返回对应的字典.py
# @Software: PyCharm

def count_letter(items):
    result = {}
    for item in items:
        if isinstance(item, (int, float)):
            result[item] = result.get(item, 0) + 1
    return result


my_list = [1, 2, 2, 2, 1, 5, 6, 1.2, 'a']

if __name__ == '__main__':
    result = count_letter(my_list)
    print(result)  # {1: 2, 2: 3, 5: 1, 6: 1, 1.2: 1}
