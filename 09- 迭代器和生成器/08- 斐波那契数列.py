#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/12 18:06
# @Author: 白云苍狗
# @File: 08- 斐波那契数列.py
# @Software: PyCharm

class Fibonacci:
    """迭代器实现斐波那契数列"""

    def __init__(self, n):
        """
        :param n: 生成数列的个数
        """
        self.n = n
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration


def fibonacci(num):
    """生成器实现斐波那契数列"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    for item in fibonacci(8):
        print(item)

    it = Fibonacci(2)
    print(next(it))
    print(next(it))
    print(next(it))