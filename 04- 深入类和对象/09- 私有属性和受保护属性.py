#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 16:09
# @Author: 白云苍狗
# @File: 09- 私有属性和受保护属性.py
# @Software: PyCharm
"""
1- 私有属性名称改写：
    如果以__mood的形式命名实例属性，那么Python就会把属性名存入实例属性__dict__中，而且会在前面加上一个下划线和类名。
    因此，对于Dog类来说，__mood会变成_Dog__mood；对于Beagle类来说，__mood会变成_Beagle_mood。
2- 受保护属性:
    Python文档的某些角落把使用一个下划线前缀标记的属性称为"受保护"的属性。
    Python解释器不会对使用单下划线的属性名做特殊处理。
    使用self._x这种形式的"保护"属性的做法很常见，但很少有人把这种属性叫做"受保护"的属性，有些人甚至将其称为"私有"属性。
3- 区别
    1. 私有属性或方法不能被子类或者其他类直接访问。
    2. 受保护属性或方法可以被子类访问，但是按照惯例，其他类或者代码不应该尝试访问它。
"""


class MyClass:
    def __init__(self):
        self.my_public_var = 'I am public'
        self._my_protected_var = 'I am protected'
        self.__my_private_var = 'I am private'

    def access_private_var(self):
        return self.__my_private_var


class MyChildClass(MyClass):
    def __init__(self):
        super().__init__()
        # 可以访问父类的公有属性
        print(self.my_public_var)
        # 可以访问父类的受保护属性
        print(self._my_protected_var)
        try:
            # 不能直接访问父类的私有属性
            print(self.__my_private_var)
        except AttributeError as e:
            print(e)

    def access_parent_private_var(self):
        # 通过父类方法访问父类的私有属性
        print(super().access_private_var())


if __name__ == '__main__':
    obj = MyClass()
    # 可以访问
    print(obj.my_public_var)  # I am public
    # 可以访问,但是不推荐
    print(obj._my_protected_var)  # I am protected
    try:
        # 不能直接访问私有属性
        print(obj.__my_private_var)  # 'MyClass' object has no attribute '__my_private_var'
    except AttributeError as e:
        print(e)
    # 通过方法访问私有属性
    print(obj.access_private_var())  # I am private

    child_obj = MyChildClass()
    """
    I am public
    I am protected
    'MyChildClass' object has no attribute '_MyChildClass__my_private_var'
    """
    # 通过父类方法访问父类的私有属性
    child_obj.access_parent_private_var()  # I am private
