#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/29 20:23
# @Author: 白云苍狗
# @File: handler_yaml.py
# @Software: PyCharm
import yaml

from interface_test.debug_talk import debug_talk
from interface_test.debug_talk.handler_debug import MyClass
from interface_test.handler_render import render_template_structure


class YamlHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_yaml(self):
        """读取并解析 YAML 文件。返回解析后的数据。"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except Exception as exc:
            print(f"处理文件时出现错误: {exc}")
            # 或者，重新抛出异常
            # raise exc

    def clear_yaml(self):
        """清空 YAML 文件内容。"""
        try:
            with open(self.file_path, 'w') as file:
                file.truncate()
        except Exception as exc:
            print(f"清空文件时出现错误: {exc}")


if __name__ == '__main__':
    yaml_handler = YamlHandler('get_token.yml')
    print(yaml_handler.read_yaml())
    """
        # 获取自定义函数
        my_object = MyClass(debug_talk)
        debug_functions = my_object.get_debug_functions
        print(debug_functions)
    
        # 使用自定义函数渲染 YAML 数据
        yaml_handler = YamlHandler('get_token.yml')
        yaml_data = yaml_handler.read_yaml()
        # 渲染后的数据
        yaml_data = render_template_structure(yaml_data, **debug_functions)
        print(yaml_data)
    """
