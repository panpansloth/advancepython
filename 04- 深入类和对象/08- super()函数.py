#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/23 15:46
# @Author: 白云苍狗
# @File: 08- super()函数.py
# @Software: PyCharm

"""
1- 坚持使用内置函数super()是确保面向对象的Python程序可维护性的基本要求。
2- 调用被覆盖的__init__方法尤其重要，可以让超类完成它负责的初始化任务。
    def __init__(self, a, b):
        super().__init__(a, b)
        ...  # 其他初始化代码
3- super()是一个内置的函数，用于在类中调用父类(超类)的方法。
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary has been raised by {amount}. New salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def raise_salary(self, amount):
        super().raise_salary(amount + self.bonus)


if __name__ == '__main__':
    e = Employee('John', 50000)
    e.raise_salary(1000)

    m = Manager('Sarah', 60000, 10000)
    m.raise_salary(1000)
