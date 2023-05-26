#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 16:11
# @Author: 白云苍狗
# @File: 01- 装饰器基础知识.py
# @Software: PyCharm

"""
1- 装饰器定义：装饰器是Python中的一种语法糖，用于在不改变函数定义的情况下，增加函数的功能。
    它接受一个函数作为参数并返回一个函数。装饰器函数通常使用@符号来表示。
2- 装饰器作用：为已经存在的对象添加额外的功能
3- 装饰器使用
    1- 定义一个装饰器函数
    2- 使用@符号将装饰器应用到函数上
        @decorator
        def target():
            print('running target()')
        上述代码的效果与下述写法一样
        def target():
            print('running target()')
        target = decorator(target)
4- 装饰器的原理
    1- 装饰器函数接受一个函数作为参数
    2- 装饰器函数内部定义一个函数，该函数接受任意数量的参数
    3- 装饰器函数内部定义的函数调用传入的函数，并将传入的参数传递给它
    4- 装饰器函数返回内部定义的函数
5- 装饰器3个基本性质
    1- 装饰器是一个函数或者其他可调用对象
    2- 装饰器可以把被装饰的函数替换成其他函数
    3- 装饰器在加载模块时立即执行
6- 装饰器的应用场景
    1- 日志记录
    2- 性能测试
    3- 认证授权
    4- 缓存
    5- 事务处理
    6- 插入日志
    7- 调试
    8- 连接池
    9- 限制资源的使用
"""


def deco(func):
    """装饰器通常会把一个函数替换成另一个函数"""

    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


# 调用被装饰的target，实际上会运行inner
target()  # running inner()
# 查看对象，发现target现在是inner的引用
print(target)  # <function deco.<locals>.inner at 0x00000162F280E9E0>
