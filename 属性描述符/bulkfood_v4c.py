#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/10/21 15:47
# @Author: 白云苍狗
# @File: bulkfood_v4c.py
# @Software: PyCharm

class Quantity:
    def __set_name__(self, owner, name):
        """
        设置各个Quantity实例的storage_name属性，即weight和price
        :param owner: 是托管类的引用，即LineItem类
        :param name: 是在托管类中定义的描述符实例的名称，即weight和price
        :return: None
        """
        self.storage_name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value + 10
        else:
            raise ValueError(f'{self.storage_name} must be > 0')



class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    # def subtotal(self):
    #     return self.weight * self.price


truffle = LineItem('White truffle', 1, 1)
print(truffle.__dict__)
