#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/8 18:51
# @Author: 白云苍狗
# @File: 04- 生成器函数.py
# @Software: PyCharm
"""
1- 只要Python函数的主体中有yield关键字，该函数就是生成器函数。调用生成器函数，返回一个生成器对象。也就是说，生成器函数是生成器工厂。
2- 生成器的工作原理：
    生成器函数创建一个生成器对象，包装生成器函数的主体。
    把生成器对象传给next()函数时，生成器函数提前执行函数主体中的下一个yield语句，返回产出的值，并在函数主体的当前位置暂停。
    最终，函数的主体返回时，Python创建的外层生成器对象抛出StopIteration异常。
3- 生成器定义
    由Python编译器构建的迭代器。为了创建生成器，我们不实现__next__方法，而是使用yield关键字得到生成器函数（创建生成器对象的工厂）。
    生成器表达式是构建生成器对象的另一种方式。生成器对象提供了__next__方法，因此生成器对象是迭代器。
"""
import re
from collections import abc

RE_WORD = re.compile(r'\w+')


class Sentence:
    """
    1. 符合Python习惯的方式：用生成器代替SentenceIterator类。
    2. 迭代器其实是生成器对象，在调用__iter__方法时自动创建，因为这里的__iter__方法是生成器方法。
    """

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({self.text!r})'

    def __iter__(self):
        """__iter__是一个生成器函数，调用时构建一个实现了Iterator接口的生成器对象，因此不再需要SentenceIterator类。"""
        for word in self.words:
            yield word


if __name__ == '__main__':
    print(issubclass(Sentence, abc.Iterator))  # False
    s = Sentence('Life of Brian')

    it = iter(s)
    print(it)  # <generator object Sentence.__iter__ at 0x000001B5EBBF0270>
    # for循环的本质
    while True:
        try:
            word = next(it)
            print(word)
        except StopIteration:
            del it
            break

    print(list(iter(s)))  # ['Life', 'of', 'Brian']
