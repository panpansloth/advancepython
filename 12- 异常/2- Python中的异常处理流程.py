#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/4 21:11
# @Author: 白云苍狗
# @File: 2- Python中的异常处理流程.py
# @Software: PyCharm

import io

# Python中的异常处理流程
try:
    # 尝试执行的代码
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    # 处理文件未找到的情况
    print("文件未找到")
else:
    # 如果没有异常发生
    print("文件读取成功")
    print(data)
finally:
    # 无论是否发生异常，都会执行的代码
    print("清理：关闭文件")
    # 检查file是否已定义并且是一个文件对象
    if "file" in locals() and isinstance(file, io.IOBase):
        file.close()

