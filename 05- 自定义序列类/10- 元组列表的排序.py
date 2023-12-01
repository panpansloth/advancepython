#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/12/1 23:30
# @Author: 白云苍狗
# @File: 10- 元组列表的排序.py
# @Software: PyCharm
"""
使用 itemgetter 排序一个元组列表
"""
from operator import itemgetter

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
