#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 21:42
# @Author: 白云苍狗
# @File: 无重复字符的最长子串.py
# @Software: PyCharm
"""
3. 无重复字符的最长子串
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

"""


def length_of_longest_substring(s):
    # 滑动窗口
    # 用一个哈希表hashmap记录每个字符最后一次出现的位置
    # 然后用一个变量start记录不重复子串的开始位置
    # 当遇到重复字符时，将开始位置移动到重复字符的下一个位置
    # 比较当前子串长度和最大长度，取较大者
    hashmap = {}
    start = 0
    max_len = 0
    l = []
    for index, ch in enumerate(s):
        if hashmap.get(ch) is not None:
            start = max(start, hashmap.get(ch) + 1)
        hashmap[ch] = index
        max_len = max(max_len, index - start + 1)

    return max_len


if __name__ == '__main__':
    s = 'abcrabcbb'
    print(length_of_longest_substring(s))
