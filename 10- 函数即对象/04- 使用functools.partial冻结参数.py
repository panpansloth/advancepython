#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/28 15:22
# @Author: 白云苍狗
# @File: 04- 使用functools.partial冻结参数.py
# @Software: PyCharm

# functools.partial高阶函数可以根据提供的可调用对象，创建一个新的可调用对象，把原函数的某些参数固定。
# functools.partial的第一个参数是一个可调用对象，后面跟着任意个要绑定的定位参数和关键字参数。
# functools.partial的实例有一个属性func，调用这个属性会调用原函数，把缺少的参数补齐。

from functools import partial
from operator import mul

triple = partial(mul, 3)
print(triple(7))  # 21
print(list(map(triple, range(1, 10))))  # [3, 6, 9, 12, 15, 18, 21, 24, 27]


