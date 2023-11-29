#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/28 20:27
# @Author: 白云苍狗
# @File: pytest断言.py
# @Software: PyCharm
import pytest


def test_equal():
    assert 1 == 1


def test_greater():
    assert 1 > 0


def test_in():
    assert "h" in "hello"


def test_list():
    assert 1 in [1, 2, 3]


def test_dict():
    assert "a" in {"a": 1, "b": 2}


if __name__ == '__main__':
    pytest.main(["-s", "pytest断言.py"])
