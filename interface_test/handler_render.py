#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/27 19:09
# @Author: 白云苍狗
# @File: handler_render.py
# @Software: PyCharm

"""
使用给定上下文递归呈现模板结构（字符串、字典或列表）。
"""
from jinja2 import Template


def render_template_structure(template_structure, **context):
    """
    Recursively render a template structure (string, dictionary, or list)
    with the given context.
    """
    if isinstance(template_structure, str):
        return Template(template_structure, variable_start_string='${', variable_end_string='}').render(**context)
    elif isinstance(template_structure, dict):
        return {key: render_template_structure(value, **context) for key, value in template_structure.items()}
    elif isinstance(template_structure, list):
        return [render_template_structure(item, **context) for item in template_structure]
    else:
        return template_structure


# Example Usage
if __name__ == '__main__':
    variables = {
        "username": "${user()}",
        "password": "123456",
        "age": "${age}",
        "data": {
            "key": "${user()}",
            "name": ["x", {"info": {"x": "1", "y": "${user()}"}}]
        }
    }

    def user():
        return 'panpan'




    age = 22
    result = render_template_structure(variables, user=user, age=age)
    print(result)
