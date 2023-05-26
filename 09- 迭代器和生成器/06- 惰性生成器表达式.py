#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/8 21:11
# @Author: 白云苍狗
# @File: 06- 惰性生成器表达式.py
# @Software: PyCharm
import re

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({self.text!r})'

    def __iter__(self):
        # 生成器表达式是语法糖，完全可以替换成生成器函数。
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('Life of Brian')
    print(list(iter(s)))  # ['Life', 'of', 'Brian']

    it = iter(s)
    print(it)  # <generator object Sentence.__iter__.<locals>.<genexpr> at 0x00000229C7C283C0>

    print(next(it))  # Life
    print(next(it))  # of
    print(next(it))  # Brian
    print(list(it))  # []
    print(next(it))  # StopIteration
