#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 11:00
# @Author: 白云苍狗
# @File: 06- 多重继承和方法的解析顺序.py
# @Software: PyCharm

"""
1- 任何实现多重继承的语言都要处理潜在的命名冲突，这种冲突由超类实现同名方法时引起。我们称之为"菱形问题"。
2- 方法解析顺序只决定唤醒顺序，至于各个类中相应的方法是否被唤醒，则取决于实现方法时，有没有调用super()。
3- 调用super的方法叫协作方法。利用协作方法可以实现多重继承。在B类中，ping是协作方法，而pong则不是。
"""


class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


leaf = Leaf()
if __name__ == '__main__':
    # 每个类都有名为__mro__的属性，它的值是一个元组，按照方法解析顺序列出各个超类，从当前类一直到object类。
    print(Leaf.__mro__)
    """
    (<class '__main__.Leaf'>, 
    < class '__main__.A' >, 
    < class '__main__.B' >, 
    < class '__main__.Root' >, 
    < class 'object' > )
    """
    # 调用leaf.ping()，唤醒Leaf、A、B和Root中的ping方法，因为前3个类中ping方法都调用了super().ping()。
    leaf.ping()
    """
    <instance of Leaf>.ping() in Leaf
    <instance of Leaf>.ping() in A
    <instance of Leaf>.ping() in B
    <instance of Leaf>.ping() in Root
    """
    # 调用leaf.pong()，唤醒继承树上A中的pong，而它又调用了super().pong()，唤醒了B.pong()。
    leaf.pong()
    """
    <instance of Leaf>.pong() in A
    <instance of Leaf>.pong() in B
    """
