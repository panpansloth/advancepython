#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 23:06
# @Author: 白云苍狗
# @File: 11- 参数化clock装饰器.py
# @Software: PyCharm
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result!r}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in args)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate


if __name__ == '__main__':
    @clock()
    def factorial(n):
        """计算阶乘"""
        return 1 if n < 2 else n * factorial(n - 1)


    # factorial = clock()(factorial)
    # factorial(6)


    print('*' * 40, 'Calling factorial(6)')
    print('6!=', factorial(6))
