#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 17:10
# @Author: 白云苍狗
# @File: 02- Python何时执行装饰器.py
# @Software: PyCharm

"""
1. Python何时执行装饰器
    1.1 装饰器在导入模块时立即执行
    1.2 装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即Python加载模块时）
    1.3 也就是说，装饰器的调用比被装饰的函数的调用早
"""
registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
    """
    running register(<function f1 at 0x000002255823EC20>)
    running register(<function f2 at 0x000002255823EDD0>)
    running main()
    registry -> [<function f1 at 0x000002255823EC20>, <function f2 at 0x000002255823EDD0>]
    running f1()
    running f2()
    running f3()
    """


if __name__ == '__main__':
    # main()
    pass