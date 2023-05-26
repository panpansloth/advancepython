#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/4/21 18:35
# @Author: 白云苍狗
# @File: 01-  鸭子类型和多态.py
# @Software: PyCharm

# 鸭子类型：当你看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
# 多态：多态是指同一种事物在不同情况下(有不同的表现形式)有多种形态。
class Dog:
    def eat(self):
        print('狗吃肉')


class Cat:
    def eat(self):
        print('猫吃鱼')


class Duck:
    def eat(self):
        print('鸭子吃虫子')


animal_list = [Dog(), Cat(), Duck()]
for animal in animal_list:
    animal.eat()
