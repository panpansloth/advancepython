#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 16:07
# @Author: 白云苍狗
# @File: 09- 使用functools.cache做备忘.py
# @Software: PyCharm
"""
@functools.cache：实现了备忘录，这是一项优化技术，能把耗时的函数得到的结果保存起来，避免传入相同的参数时重复计算。
叠放装饰器：@是一种语法糖，其作用是把装饰器函数应用到下方函数上。多个装饰器的行为就像调用嵌套函数一样。
    @alpha
    @beta
    def my_fn():
        ...
    等同于以下内容：
    my_fn = alpha(beta(my_fn))
    也就是说，首先应用beta装饰器，然后再把返回的函数传给alpha。
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


@functools.cache
@clock  # @cache应用到@clock返回的函数上
def fibonacci(n):
    """生成第n个斐波那契数"""
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
    """
    [0.00000030s] fibonacci(['0']) -> 0
    [0.00000020s] fibonacci(['1']) -> 1
    [0.00002790s] fibonacci(['2']) -> 1
    [0.00000050s] fibonacci(['3']) -> 2
    [0.00003630s] fibonacci(['4']) -> 3
    [0.00000030s] fibonacci(['5']) -> 5
    [0.00004380s] fibonacci(['6']) -> 8
    8
    """
