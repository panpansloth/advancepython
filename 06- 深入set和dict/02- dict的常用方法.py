#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:36
# @Author: 白云苍狗
# @File: 02- dict的常用方法.py
# @Software: PyCharm

"""
https://www.programiz.com/python-programming/methods/dictionary
# 1. 删除所有项
d.clear()
# 2. 浅拷贝
d.copy()
# 3. 根据可迭代对象中的键构建一个映射，可选参数initial指定初始值，默认为None
d.fromkeys(it, [initial])
# 4. 获取键k对应的项，不存在时返回default或者None
d.get(k, [default])
# 5. 如果d中有键k，则返回d[k]；否则，把d[k]设为default，并返回default
d.setdefault(k, [default])
# 6. 使用映射或可迭代对象中的键值对更新d
# 先检查m有没有keys方法，如果有，则假定m是映射；否则退而求其次，迭代m，假定项是键值对形式((key, value))。
# 多数Python映射的构造函数，内部逻辑与update()方法一样，也就是说，可以从其他映射或者生成键值对的可迭代对象初始化。
d.update(m, [**kwargs])  # d.update(((key, value)))
"""

