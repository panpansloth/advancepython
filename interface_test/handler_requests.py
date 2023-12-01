#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/27 15:49
# @Author: 白云苍狗
# @File: handler_requests.py
# @Software: PyCharm
"""
requests基本使用：
1- 安装：pip install requests教程
2- 导入：import requests教程
3- 发起请求：
    1. get请求：response = requests.get(url, params=None, **kwargs)
    2. post请求：response = requests.post(url, data=None, json=None, **kwargs)
    3. put请求：response = requests.put(url, data=None, **kwargs)
    4. delete请求：response = requests.delete(url, **kwargs)
    5. head请求：response = requests.head(url, **kwargs)
    6. options请求：response = requests.options(url, **kwargs)
    7. patch请求：response = requests.patch(url, data=None, **kwargs)
    8. request请求：response = requests.request(method, url, **kwargs)
4- 响应对象：
    1. 响应状态码：response.status_code
    2. 响应头：response.headers
    3. 响应体：response.text
    4. 响应体：response.content
    5. 响应体：response.json()
"""
import os
import requests


class RequestHandler:
    session = requests.Session()

    @staticmethod
    def handle_request(value, base_url):
        """
        Handle an HTTP request based on the provided parameters.
        :param value: Dictionary containing the request parameters.
        :param base_url: Base URL for the request.
        :return: Response object.
        """
        if not value:
            raise ValueError('Request parameters are None')

        url = base_url + value.pop('url')
        method = value.pop('method')

        response = RequestHandler._send_request(method, url, value)
        # print(response.json())
        return response

    @staticmethod
    def _send_request(method, url, parameters):
        """Send the HTTP request."""
        if files := parameters.get('files'):
            for file_key, file_path in files.items():
                # Assuming file_path is the path to the file
                if os.path.exists(file_path):
                    files[file_key] = open(file_path, 'rb')
                else:
                    raise FileNotFoundError(f"File {file_path} not found")

        response = RequestHandler.session.request(method, url, **parameters)
        if not response.ok:
            response.raise_for_status()
        return response


handler = RequestHandler()

# Example Usage
if __name__ == '__main__':
    _base_url = 'https://httpbin.org'
    _value = {"url": "/post", "method": "post", "data": {"name": "panpan"}, "files": {"file": "foo.png"}}
    _response = handler.handle_request(_value, _base_url)
    print(_response.json())
