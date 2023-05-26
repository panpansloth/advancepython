#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:44
# @Author: 白云苍狗
# @File: 02- 序列是可迭代的.py
# @Software: PyCharm

import re

RE_WORD = re.compile('\w+')


class Sentence:
    """实现序列协议，这个类的对象可以迭代，因为所有序列都是可迭代的。"""

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({self.text!r})'


if __name__ == '__main__':
    s = Sentence('Life of Brian')
    it = iter(s)
    print(it)  # <iterator object at 0x000001A942CB3880>
    # 因为可以迭代，所以Sentence对象可用于构建列表和其他可迭代类型。
    print(list(s))  # ['Life', 'of', 'Brian']
