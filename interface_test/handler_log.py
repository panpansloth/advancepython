#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/30 12:40
# @Author: 白云苍狗
# @File: handler_log.py
# @Software: PyCharm

import logging
import os
import time

FMT = '[%(asctime)s] %(levelname)s %(filename)s[%(lineno)d]: %(message)s'

log_path = os.path.join(os.path.dirname(__file__), 'logs')


def setup_logger(level=logging.INFO, fmt=FMT):
    log_dir = os.path.join(log_path, f"{time.strftime('%Y-%m-%d %H%M')}.log")
    # 创建日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    # 创建日志格式
    formatter = logging.Formatter(fmt)

    # 创建控制台处理器并设置级别和格式
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # 创建文件处理器并设置级别和格式
    file_handler = logging.FileHandler(log_dir, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


my_logger = setup_logger()
if __name__ == '__main__':
    my_logger.info('这是一条信息级别的日志')
    my_logger.error('这是一条错误级别的日志')
