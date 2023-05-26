#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/8 18:16
# @Author: 白云苍狗
# @File: 03- 经典迭代器.py
# @Software: PyCharm
import re
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({self.text!r})'

    def __iter__(self):
        """根据可迭代协议，__iter__方法实例化并返回一个迭代器。"""
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


if __name__ == '__main__':
    print(issubclass(SentenceIterator, abc.Iterator))  # True
    s = Sentence('Life of Brian')

    it = iter(s)
    print(it)  # <__main__.SentenceIterator object at 0x0000025971943580>
    for word in it:
        print(word)
    print(list(it))  # []

    print(list(iter(s)))  # ['Life', 'of', 'Brian']
