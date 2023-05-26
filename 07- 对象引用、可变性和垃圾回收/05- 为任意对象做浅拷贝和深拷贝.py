#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/26 10:57
# @Author: 白云苍狗
# @File: 05- 为任意对象做浅拷贝和深拷贝.py
# @Software: PyCharm
"""
1- 构造函数或[:]做的是浅拷贝，即复制最外层容器，副本中的项是源容器中项的引用。
2- 深拷贝，副本不共享内部对象的引用。
3- copy模块提供的copy和deepcopy函数分别对任意对象做浅拷贝和深拷贝。
"""
import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        # 学生上车
        self.passengers.append(name)

    def drop(self, name):
        # 学生下车
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])

bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))  # 2428470247136 2428470246704 2428470246032
bus1.drop('Bill')
print(bus2.passengers)  # ['Alice', 'Claire', 'David']
# 查看passengers属性后发现，bus1和bus2共享同一个列表对象，因为bus2是bus1的浅拷贝副本。
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))  # 2804043213376 2804043213376 2804042334272
# bus3是bus1的深拷贝副本，因此它的passengers属性引用另一个列表。
print(bus3.passengers)  # ['Alice', 'Bill', 'Claire', 'David']
