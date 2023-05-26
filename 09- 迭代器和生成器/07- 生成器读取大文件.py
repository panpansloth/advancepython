#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:45
# @Author: 白云苍狗
# @File: 07- 生成器读取大文件.py
# @Software: PyCharm

"""
1. 第一个参数必须是一个可迭代对象，重复调用（不传入参数）产生值；
2. 第二个参数是哨符，即一种标记值。如果可调用对象返回哨符，则迭代器抛出StopIteration异常，而不产生哨符。
"""
from functools import partial
from random import randint


def chunked_file_reader(file_path, chunk_size=1024):
    """
    生成器函数，每次读取指定大小的文件内容。
    :param file_path: 文件路径
    :param chunk_size: 每次读取的文件大小
    :return: 每次读取的文件内容
    """
    with open(file_path, encoding='utf-8') as f:
        read1024 = partial(f.read, chunk_size)
        # print(callable(read1024))  # True
        for chunk in iter(read1024, ''):
            yield chunk


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)

if __name__ == '__main__':
    print(callable(d6))  # True
    print(d6_iter)  # <callable_iterator object at 0x000001E3FD7C3DF0>
    for roll in d6_iter:
        print(roll)

    for chunk in chunked_file_reader('test.txt', 1024):
        print(chunk)
