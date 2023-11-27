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
4- 总结：传递“引用的副本”允许函数访问和修改外部传入的对象，但这个机制也确保了对引用本身的重新赋值不会影响到外部变量的引用。
"""


def modify_list(my_list):
    print(f'Inside function before modification: my_list = {my_list}, id(my_list) = {id(my_list)}')
    # 这会修改原始列表
    my_list.append(4)
    # 这只改变了局部变量my_list的值，不影响原始列表
    my_list = [7, 8, 9]
    print(f'Inside function after modification: my_list = {my_list}, id(my_list) = {id(my_list)}')


if __name__ == '__main__':
    param = [1, 2, 3]
    print(f'Outside function call: param = {param}, id(param) = {id(param)}')
    modify_list(param)
    print(f'Outside function call: param = {param}, id(param) = {id(param)}')
