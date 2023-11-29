#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/28 20:36
# @Author: 白云苍狗
# @File: conftest.py
# @Software: PyCharm
import pytest

"""
1- 固件作用域在定义固件时通过 scope 参数设置作用域
@pytest.fixture(scope="module")
function:
默认作用域。每个测试函数调用一次固件。对于大多数测试，这是最常用的作用域。
class:
当你有一个类包含多个测试方法时，固件在该类的第一个测试方法之前被设置，最后一个测试方法之后被销毁。
适用于需要在同一个类中的多个测试方法之间共享固件的情况。
module:
固件对整个模块只创建一次，适用于所有在模块中的测试函数。
当固件在模块中的多个测试函数间共享且设置和销毁成本较高时（如数据库连接），这种作用域特别有用。
package:
固件在整个包（Python package）的第一个测试之前创建，最后一个测试之后销毁。
这个作用域对于跨多个模块的固件共享特别有用，但不太常用。
session:
固件在整个测试会话期间只创建一次和销毁一次。
适用于跨整个项目的测试共享，比如配置测试环境或外部资源的连接。

2- 自动使用的固件@pytest.fixture(autouse=True)：
自动使用的固件在整个测试过程中可能会影响所有测试，因此在使用时应当考虑其对测试环境的潜在影响。
对于只在特定测试中需要的固件，通常最好不要设置为自动使用，以保持测试的清晰和明确。

3- pytest.mark.usefixtures：这个标记主要用于那些只负责设置和清理，而不需要返回值的固件。

"""



# demo1：定义普通固件
@pytest.fixture
def database_connection():
    # 假设这是创建数据库连接的代码
    connection = "Database Connection"
    yield connection  # 提供连接给测试用例
    # 断开数据库连接
    connection = None


# demo2：定义自动使用的固件@pytest.fixture(autouse=True)
# 当固件被设置为自动使用时，它会在指定作用域内的每个测试函数运行之前自动被调用。
@pytest.fixture(autouse=True)
def print_messages():
    print("开始一个测试")
    yield
    print("测试结束")


# 使用固件
def test_database_query(database_connection):
    # 这里可以使用 database_connection
    assert database_connection is not None
    # 进行数据库查询等操作


# 使用 pytest.mark.usefixtures 在测试函数中使用固件
@pytest.mark.usefixtures("print_messages")
def test_database_operations():
    assert True  # 这里可以是对数据库的操作
