#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:37
# @Author: 白云苍狗
# @File: 03- dict的子类.py
# @Software: PyCharm

# dict子类的一个例子
class StrKeyDict0(dict):
    """
    StrKeyDict0的实例把非字符串的键转换为字符串
    """

    def __missing__(self, key):
        """
        __missing__方法是所有映射类型都可以选择去实现的方法，为了在查询的时候，如果找不到键，能够自动调用该方法
        :param key:
        :return:
        """
        # 如果找不到的键本身就是字符串，那就抛出异常
        if isinstance(key, str):
            raise KeyError(key)
        # 如果找不到的键不是字符串，那就把它转换成字符串再查找
        return self[str(key)]

    def get(self, key, default=None):
        """
        get方法把查找工作用self[key]的形式委托给__getitem__，这样在宣布查找失败之前，还能通过__missing__再给某个键一个机会
        :param key:
        :param default:
        :return:
        """
        try:
            # get方法把查找工作用self[key]的形式委托给__getitem__，这样在宣布查找失败之前，还能通过__missing__再给某个键一个机会
            return self[key]
        except KeyError:
            # 如果抛出KeyError，说明__missing__也失败了，返回default
            return default

    def __contains__(self, key):
        """
        __contains__方法用in操作符会调用这个方法
        :param key:
        :return:
        """
        # 先按照原本的方法查找，如果失败了，再把键转换成字符串再查找一次
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])  # two
    print(d[4])  # four
    try:
        print(d[1])
    except KeyError as e:
        print(e)  # '1'
    print(d.get('2'))  # two
    print(d.get(4))  # four
    print(d.get(1, 'N/A'))  # N/A
    print(2 in d)  # True
    print(1 in d)  # False
