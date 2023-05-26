#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/4 17:09
# @Author: 白云苍狗
# @File: 07- 列表推导式、生成器表达式和字典推导式.py
# @Software: PyCharm

# 列表推导式
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)  # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

# 生成器表达式
for tshirt in (f'{color} {size}' for color in colors for size in sizes):
    print(tshirt)

# 字典推导式
dial_codes = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan')]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)  # {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92}
code_tail = {code: country for country, code in country_dial.items() if code > 50}
print(code_tail)  # {86: 'China', 91: 'India', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan'}
