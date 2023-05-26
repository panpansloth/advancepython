#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 14:44
# @Author: 白云苍狗
# @File: 03- 用户定义的可调用对象.py
# @Software: PyCharm

"""
1. 函数是一种可调用对象
2. 除了用户定义的函数，调用运算符（即()）还可以应用到其他对象上。
3. 如果想判断对象能否调用，可以使用内置的callable()函数。
4. 不仅Python函数是真正的对象，任何Python对象都可以表现得像函数。为此只需实现__call__实例方法。

__call__方法作用：
__call__方法是创建类似函数对象的简便方式。
__call__的另一个用处是实现装饰器。
"""
import random


class BingoCage:
    """
    BingoCage的实例使用任何可迭代对象构建，而且会在内部存储一个随机顺序的列表，调用实例从中取出一个元素。
    """

    def __init__(self, items):
        self._items = list(items)
        # shuffle打乱顺序
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))

if __name__ == '__main__':
    print(bingo.pick())  # 0
    print(bingo())  # 1
    print(callable(bingo))  # True
