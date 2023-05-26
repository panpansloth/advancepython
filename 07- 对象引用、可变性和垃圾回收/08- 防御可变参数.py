#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/26 13:20
# @Author: 白云苍狗
# @File: 08- 防御可变参数.py
# @Software: PyCharm

"""
1- 防御可变参数
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # 预防可变参数正确的做法是，自己维护列表，创建passengers的副本。
            self.passengers = list(passengers)

2- 除非方法确实想修改通过参数传入的对象，否则在类中直接把参数赋值给实例变量之前一定要三思，因为这样会为参数对象创建别名。
"""


class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # 传给构造方法的列表创建了别名
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
# 在self.passengers上调用.remove()和.append()方法，其实会修改传给构造方法的列表
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)  # ['Sue', 'Maya', 'Diana']
