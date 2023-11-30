#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/29 20:04
# @Author: 白云苍狗
# @File: handler_debug.py
# @Software: PyCharm


import inspect


class MyClass:
    def __init__(self, debug_module):
        self.debug_module = debug_module

    @property
    def get_debug_functions(self):
        """
        获取 debug_module 中的所有函数
        """
        return dict(inspect.getmembers(self.debug_module, inspect.isfunction))



if __name__ == '__main__':
    import debug_talk

    my_object = MyClass(debug_talk)
    debug_functions = my_object.get_debug_functions
    print(debug_functions)


