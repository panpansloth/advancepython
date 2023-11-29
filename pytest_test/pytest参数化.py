#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/28 20:17
# @Author: 白云苍狗
# @File: pytest参数化.py
# @Software: PyCharm

"""
pytest参数化
"""
import pytest


def add(x, y):
    return x + y


@pytest.mark.parametrize("x,y,expected", [(1, 1, 2), (1, 0, 1), (0, 0, 0)])
def test_add(x, y, expected):
    assert add(x, y) == expected


def test_add1():
    assert add(1, 1) == 2
