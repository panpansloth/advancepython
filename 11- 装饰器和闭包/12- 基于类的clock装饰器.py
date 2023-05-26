#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 23:17
# @Author: 白云苍狗
# @File: 12- 基于类的clock装饰器.py
# @Software: PyCharm
"""
通过定义__call__方法的类实现了参数化装饰器clock
"""
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result!r}'


class Clock:
    """Clock类是参数化装饰器工厂"""
    def __init__(self, fmt=DEFAULT_FMT):
        # Clock(my_format)传入的参数赋值给这里的fmt参数。
        # 类构造函数返回一个clock实例，my_format被存储为self.fmt。
        self.fmt = fmt

    def __call__(self, func):
        # 有了__call__方法，clock实例就成为了可调用对象了。
        # 可调用实例的结果是把被装饰器的函数替换成clocked。
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in args)
            print(self.fmt.format(**locals()))
            return result

        return clocked


if __name__ == '__main__':
    @Clock()
    def factorial(n):
        """计算阶乘"""
        return 1 if n < 2 else n * factorial(n - 1)


    # factorial = Clock()(factorial)
    # factorial(6)

    print('*' * 40, 'Calling factorial(6)')
    print('6!=', factorial(6))
