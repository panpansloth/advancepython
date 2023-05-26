#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/22 0:33
# @Author: 白云苍狗
# @File: 07- @classmethod、@staticmethod和实例方法.py
# @Software: PyCharm
"""
classmethod装饰器：
    1. 类装饰器定义操作类而不是操作实例的方法。
    2. 类装饰器改变了调用方法的方式，因此接收的第一个参数是类本身，而不是实例。
    3. 类装饰器最常见的用途是定义备选构造函数。

staticmethod装饰器：
    1. 静态方法就是普通函数，只是碰巧位于类的定义体中，而不是在模块层定义。

区别：
    1. 类方法接收一个隐含的类参数cls，只能访问类变量或方法，不能访问实例变量或方法。
    2. 静态方法不接受特殊的第一个参数，无法访问类或实例的属性或方法，它主要用来做一些独立于类和实例的工作。
"""


class MyClass:
    class_var = 'I am a class var'

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @classmethod
    def my_class_method(cls):
        print(cls.class_var)
        try:
            print(cls.instance_var)
        except AttributeError as e:
            print(e)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        """备选构造方法，可以接受不同格式的输入，然后返回一个新的类实例"""
        name, age = string.split(',')
        return cls(name, int(age))

    def __str__(self):
        return f'{self.name}, {self.age}'


if __name__ == '__main__':
    MyClass.my_class_method()
    """
    I am a class var
    type object 'MyClass' has no attribute 'instance_var'
    """

    p1 = Person('Tom', 20)
    print(p1)  # Tom, 20
    p2 = Person.from_string('Jerry, 18')
    print(p2)  # Jerry, 18
