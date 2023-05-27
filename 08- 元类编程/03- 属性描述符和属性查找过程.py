#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 20:41
# @Author: 白云苍狗
# @File: 03- 属性描述符和属性查找过程.py
# @Software: PyCharm
"""
1- 在Python中，当你访问对象的一个属性时（object.attribute），访问优先级从高到低：
    1- __getattribute__优先级最高的函数，所有对属性的访问必先访问它
    2- 覆盖型描述符（数据描述符）
    3- 实例属性 object.__dict__
    4- 类属性
    5- 非覆盖型描述符
    6- 父类的属性，父类中定义的属性也是子类的属性
    7- __getattr__，是一个“后备”属性，当所有查找都失败时，才调用__getattr__。
    8- 如果没有定义__getattr__，会抛出AttributeError异常。
2- 属性描述符：必须定义为类变量，而不能定义为实例变量
    1- 覆盖型描述符（数据描述符）：实现了 __get__ 和 __set__ 方法。如果一个对象定义了 __set__，那么它就被认为是一个数据描述符。
    2- 非覆盖型描述符（非数据描述符）：只实现了 __get__ 方法。不会覆盖对实例属性的赋值操作。
3- 描述符工作机制
    1- 如果你把描述符定义为实例变量，那么当你尝试访问这个属性时，
    Python 会直接返回描述符对象本身，而不是调用描述符的 __get__ 或 __set__ 方法。
    2- 当你尝试访问一个属性时，Python 会首先在类的层次结构中查找这个属性，
    如果找到了一个描述符（一个定义了 __get__ 或 __set__ 或 __delete__ 方法的对象），那么 Python 将会调用描述符的相应方法。
"""


# TODO: 补充属性描述符和属性查找过程的例子

class Descriptor:
    """
    Descriptor 是一个描述符类，包含 __get__ 和 __set__ 方法，所以它是一个数据描述符。
    """

    def __get__(self, instance, owner):
        print("Descriptor __get__")
        return 'Descriptor value'

    def __set__(self, instance, value):
        print("Descriptor __set__")


class MyClass:
    # attr 是一个数据描述符
    attr = Descriptor()
    attr_class = 'Class attribute value'

    def __init__(self):
        self.attr_instance = 'Instance attribute value'

    def __getattribute__(self, item):
        print("MyClass __getattribute__")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("MyClass __getattr__")
        return 'Default value'


if __name__ == '__main__':
    # 创建 MyClass 的实例
    mc = MyClass()

    # 获取 attr 属性时，首先调用 MyClass 的 __getattribute__ 方法。
    # 因为 attr 是一个数据描述符，调用 Descriptor 的 __get__ 方法。
    print(mc.attr)
    """
    MyClass __getattribute__
    Descriptor __get__
    Descriptor value
    """

    print(mc.attr_class)
    """
    MyClass __getattribute__
    Class attribute value
    """

    # 获取 attr_instance 属性时，首先调用 MyClass 的 __getattribute__ 方法。
    # 因为 attr_instance 存在于实例的 __dict__ 中，所以直接返回它。
    print(mc.attr_instance)
    """
    MyClass __getattribute__
    Instance attribute value
    """

    # 获取不存在的属性 non_existing_attr 时，首先调用 MyClass 的 __getattribute__ 方法。
    # 因为 non_existing_attr 既不存在于实例的 __dict__ 中，又不是一个描述符，所以调用 MyClass 的 __getattr__ 方法。
    print(mc.non_existing_attr)
    """
    MyClass __getattribute__
    MyClass __getattr__
    Default value
    """
