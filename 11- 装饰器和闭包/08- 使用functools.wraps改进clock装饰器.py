#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 15:56
# @Author: 白云苍狗
# @File: 08- 使用functools.wraps改进clock装饰器.py
# @Software: PyCharm
"""
@functools.wraps：pass
"""
import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k} = {v!r}' for k, v in kwargs.items())
        print(f'[{elapsed:0.8f}s] {name}({arg_lst}) -> {result!r}')
        return result

    return clocked


@clock
def factorial(n):
    """计算n的阶乘"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(n=6))  # 720
    print(factorial.__name__)  # factorial
    print(factorial.__doc__)  # 计算n的阶乘
