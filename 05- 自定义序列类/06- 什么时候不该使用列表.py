#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/4 17:09
# @Author: 白云苍狗
# @File: 06- 什么时候不该使用列表.py
# @Software: PyCharm
"""
    1. 如果经常需要在列表的两端添加和删除项，使用collections.deque。
    2. 如果一个列表只包含数值，那么使用array.array更高效。
    3. 如果在代码中经常检查容器中是否存在某一项，应考虑使用set类型存储my_collection。

"""
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.appendleft(-1)
print(dq)  # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)
dq.append(10)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 10], maxlen=10)
dq.extend([11, 12, 13])
print(dq)  # deque([3, 4, 5, 6, 7, 8, 10, 11, 12, 13], maxlen=10)
dq.pop()
dq.popleft()
print(dq)  # deque([4, 5, 6, 7, 8, 10, 11, 12], maxlen=10)
