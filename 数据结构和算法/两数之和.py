#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/5/17 18:16
# @Author: 白云苍狗
# @File: 两数之和.py
# @Software: PyCharm

# 1. 两数之和
# https://leetcode-cn.com/problems/two-sum/
# 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。

def two_sum(nums, target):
    # 暴力枚举
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum1(nums, target):
    # 哈希表
    hashmap = {}
    for index, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [hashmap.get(target - num), index]
        hashmap[num] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum1(nums, target))

