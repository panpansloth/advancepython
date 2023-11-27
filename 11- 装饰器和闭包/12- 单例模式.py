#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/12 17:40
# @Author: 白云苍狗
# @File: 12- 单例模式.py
# @Software: PyCharm
"""
单例模式：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
单例模式的应用场景：
    1. 资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置。
    2. 控制资源的情况下，方便资源之间的互相通信，如线程池等。
"""

# 1. 使用装饰器实现单例模式
def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


# 2. 重写__new__方法实现单例模式
class Singleton:
    instance = None
    init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        if Singleton.init_flag:
            self.name = name
            Singleton.init_flag = False


if __name__ == '__main__':
    @singleton
    class A:
        def __init__(self, x):
            self.x = x


    a1 = A(1)
    a2 = A(2)
    print(a1.x, a2.x)  # 1 1
    print(a1 is a2)  # True
    print(a1 == a2)  # True

    s1 = Singleton('白云苍狗')
    s2 = Singleton('白依苍狗')
    print(s1, s2)  # <__main__.Singleton object at 0x0000020F7F6F4E80> <__main__.Singleton object at 0x0000020F7F6F4E80>
