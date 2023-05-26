#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/26 13:35
# @Author: 白云苍狗
# @File: 06- 共享传参.py
# @Software: PyCharm

"""
1- Python唯一支持的参数传递模式是共享传参。
2- 共享传参指函数的形参获得实参引用的副本。也就是说，函数内部的形参是实参的别名。
3- 共享传参的结果是，函数可能会修改作为参数传入的可变对象，但是无法修改哪些对象的标识。
"""


def modify(my_list):
    """
    即使形参获取的是实参引用的副本，但对形参的引用本身的修改不会影响到实参的引用。
    然而，如果引用的对象是可变的，那么我们可以通过修改形参来修改实参所引用的对象。
    :param my_list: 列表
    """
    print(f'Inside function before modification: my_list = {my_list}, id(my_list) = {id(my_list)}')
    # 修改了形参p所引用的对象（即，向列表中添加了一个元素）
    my_list.append(4)
    # 修改了p的引用本身（即，将p指向了一个新的列表）
    my_list = [7, 8, 9]
    print(f'Inside function after modification: my_list = {my_list}, id(my_list) = {id(my_list)}')


if __name__ == '__main__':
    param = [1, 2, 3]
    print(f'Outside function call: param = {param}, id(param) = {id(param)}')
    modify(param)
    print(f'Outside function call: param = {param}, id(param) = {id(param)}')
    """
    Outside function call: param = [1, 2, 3], id(param) = 2693342621760
    Inside function before modification: my_list = [1, 2, 3], id(my_list) = 2693342621760
    Inside function after modification: my_list = [7, 8, 9], id(my_list) = 2693342850496
    Outside function call: param = [1, 2, 3, 4], id(param) = 2693342621760
    """
