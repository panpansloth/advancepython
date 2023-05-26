#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/8 21:05
# @Author: 白云苍狗
# @File: 05- 惰性生成器.py
# @Software: PyCharm
import re

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({self.text!r})'

    def __iter__(self):
        # re.finditer函数是re.findall函数的惰性版本，返回的不是列表，而是一个生成器对象，按需产出re.MatchObject实例。
        for match in RE_WORD.finditer(self.text):
            # match.group()方法从MatchObject实例中提取匹配的文本。
            yield match.group()


if __name__ == '__main__':
    s = Sentence('Life of Brian')
    print(list(iter(s)))  # ['Life', 'of', 'Brian']

    it = iter(s)
    print(it)  # <generator object Sentence.__iter__ at 0x00000214666DC2E0>

    print(next(it))  # Life
    print(next(it))  # of
    print(next(it))  # Brian
    print(list(it))  # []
    print(next(it))  # StopIteration
