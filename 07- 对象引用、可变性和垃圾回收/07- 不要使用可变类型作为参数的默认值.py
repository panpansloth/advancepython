#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/26 10:58
# @Author: 白云苍狗
# @File: 07- 不要使用可变类型作为参数的默认值.py
# @Software: PyCharm
"""
1- 不要使用不可变类型作为参数的默认值
"""


class HauntedBus:
    """一个受幽灵乘客折磨的校车模型"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers)  # ['Alice', 'Bill']
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)  # ['Bill', 'Charlie']
    # bus2是空的，因此把默认的空列表分配给self.passengers
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(bus2.passengers)  # ['Carrie']
    # bus3一开始也是空的，因此还是分配默认列表
    bus3 = HauntedBus()
    print(bus3.passengers)  # ['Carrie']
    bus3.pick('Dave')
    print(bus2.passengers)  # ['Carrie', 'Dave']
    # bus2.passengers和bus3.passengers指代同一个列表
    print(bus2.passengers is bus3.passengers)  # True
    # bus1.passengers指代不同列表
    print(bus1.passengers)  # ['Bill', 'Charlie']
    # 查看HauntedBus.__init__对象，看看它的__defaults__属性中的哪些幽灵乘客
    print(HauntedBus.__init__.__defaults__)  # (['Carrie', 'Dave'],)
    # 验证bus2.passengers是一个别名，绑定HauntedBus.__init__.__defaults__属性的第一个元素
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)  # True
