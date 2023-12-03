#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/12/3 14:05
# @Author: 白云苍狗
# @File: demo.py
# @Software: PyCharm


import requests
import requests_mock


# 被测试的函数
def function_to_test():
    url = 'https://httpbin.org/post'
    response = requests.post(url, data={'key': 'value'})
    return response.json()


# 测试函数
def test_mock():
    """
    使用 requests-mock 模拟 HTTP 请求
    1- requests-mock 拦截了对 https://httpbin.org/post 的 POST 请求，并返回了一个模拟的 JSON 响应。
    2- 测试验证函数 function_to_test 是否正确地返回了这个模拟的响应。
    """
    # 使用 requests-mock 创建一个上下文管理器
    with requests_mock.Mocker() as m:
        # 模拟 POST 请求并定义返回的 JSON 数据
        m.post('https://httpbin.org/post', json={'mock_key': 'mock_response'})

        # 调用函数并获取结果
        result = function_to_test()

        # 检查函数的返回值是否是我们模拟的 JSON 数据
        assert result == {'mock_key': 'mock_response'}
