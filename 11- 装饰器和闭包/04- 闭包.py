#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/29 10:40
# @Author: 白云苍狗
# @File: 04- 闭包.py
# @Software: PyCharm

"""
1- 闭包：闭包是一个函数，它保留了定义函数时存在的自由变量的绑定。这样调用函数时，虽然定义作用域不可用了，但是仍然能够使用那些绑定。
自由变量：指未在局部作用域中绑定的变量。
2- 闭包构成条件：
    1. 必须有一个内嵌函数
    2. 内嵌函数必须引用外部函数中的变量
    3. 外部函数的返回值必须是内嵌函数
"""


class Averager:
    """
    一个计算累计平均值的类
    """

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)


# Average类的实例是可调用对象
avg = Averager()
print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0


def make_averager():
    """一个计算累计平均值的高阶函数"""
    # series是make_averager函数的局部变量，因为赋值语句series = []在make_averager的定义体中。
    series = []

    def averager(new_value):
        # 在averager函数中，series是自由变量（free variable）。
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg1 = make_averager()
print(avg1(10))  # 10.0
print(avg1(11))  # 10.5
print(avg1(12))  # 11.0

# 查看make_averager函数返回的averager对象，发现在__code__属性中保存局部变量和自由变量的名称。
print(avg1.__code__.co_varnames)  # ('new_value', 'total')
print(avg1.__code__.co_freevars)  # ('series',)
# 闭包中的自由变量series，发现其绑定的是avg1.__closure__中的cell对象。
print(avg1.__closure__)  # (<cell at 0x00000176A4FA3C70: list object at 0x00000176A4F86C40>,)
print(avg1.__closure__[0].cell_contents)  # [10, 11, 12]


