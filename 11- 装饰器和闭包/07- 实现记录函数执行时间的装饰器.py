#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 14:54
# @Author: 白云苍狗
# @File: 07- 实现记录函数执行时间的装饰器.py
# @Software: PyCharm
"""
实现的装饰器有几个缺点：
    1. 不支持关键字参数。
    2. 而且遮盖了被装饰函数的__name__属性和__doc__属性。
"""
import time


class Clock:
    """类装饰器"""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        # 记录初始时间t0
        t0 = time.perf_counter()
        # 调用原来的factorial函数，保存结果
        result = self.func(*args)
        # 计算运行时间
        elapsed = time.perf_counter() - t0
        name = self.func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        # 格式化收集的数据，然后打印出来
        print(f'[{elapsed:0.8f}s] {name}({arg_str})->{result!r}')
        # 返回factorial函数结果
        return result


def clock(func):
    """函数装饰器"""

    def clocked(*args):
        # 记录初始时间t0
        t0 = time.perf_counter()
        # 调用原来的factorial函数，保存结果
        result = func(*args)
        # 计算运行时间
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        # 格式化收集的数据，然后打印出来
        print(f'[{elapsed:0.8f}s] {name}({arg_str})->{result!r}')
        # 返回factorial函数结果
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@Clock
def factorial(n):
    """计算阶乘"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(3)')
    snooze(3)
    print('*' * 40, 'Calling factorial(6)')
    print('6!=', factorial(6))
    """
    **************************************** Calling snooze(3)
    [3.00840650s] snooze(3)->None
    **************************************** Calling factorial(6)
    [0.00000080s] factorial(1)->1
    [0.00001870s] factorial(2)->2
    [0.00003290s] factorial(3)->6
    [0.00005230s] factorial(4)->24
    [0.00006510s] factorial(5)->120
    [0.00008190s] factorial(6)->720
    6!= 720
    """
