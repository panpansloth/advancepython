#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 22:42
# @Author: 白云苍狗
# @File: 10- 参数化注册装饰器.py
# @Software: PyCharm

"""
1- Python会把被装饰的函数作为第一个参数传给装饰器函数。
2- 如何让装饰器接受其他参数呢？
    创建一个装饰器工厂函数来接收那些参数，然后再返回一个装饰器，应用到被装饰的函数上。
"""
registry = set()


def register(active=True):
    def decorate(func):
        print(f'running register(active={active})->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == '__main__':
    f1()
    f3 = register()(f3)
    f3()
    print('registry->', registry)
    f2 = register(active=False)(f2)
    print('registry->', registry)
    """
    running register(active=False)->decorate(<function f1 at 0x000001E26F41E9E0>)
    running register(active=True)->decorate(<function f2 at 0x000001E26F41EC20>)
    running f1()
    running register(active=True)->decorate(<function f3 at 0x000001E26F41ECB0>)
    running f3()
    registry-> {<function f2 at 0x000001E26F41EC20>, <function f3 at 0x000001E26F41ECB0>}
    running register(active=False)->decorate(<function f2 at 0x000001E26F41EC20>)
    registry-> {<function f3 at 0x000001E26F41ECB0>}
    """