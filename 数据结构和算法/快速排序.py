#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/9 19:51
# @Author: 白云苍狗
# @File: 快速排序.py
# @Software: PyCharm
def quick_sort(alist, low, high):
    if high <= low:
        return
    # 切分
    p = partition(alist, low, high)
    # 将左半部分alist[low...p-1]排序
    quick_sort(alist, low, p - 1)
    # 将右半部分alist[p+1...high]排序
    quick_sort(alist, p + 1, high)


def partition(alist, low, high):
    """
    左指针从左向右扫描，找到第一个大于pivot的元素
    右指针从右向左扫描，找到第一个小于pivot的元素
    交换这两个元素，直到左右指针相遇
    将pivot与左右指针相遇的元素交换
    :param alist:
    :param low:
    :param high:
    :return: 左右指针相遇的位置
    """
    pivot = alist[high]
    left = low
    right = high - 1
    while True:
        # 移动左指针，直到找到一个大于或等于pivot的元素
        while left <= right and alist[left] < pivot:
            left += 1
        # 移动右指针，直到找到一个小于或等于pivot的元素
        while left <= right and alist[right] > pivot:
            right -= 1
        # 如果左指针和右指针相遇，则退出循环
        if left >= right:
            break
        # 交换左右指针指向的元素
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    # 将基准元素放在其最终位置上
    alist[left], alist[high] = alist[high], alist[left]
    # 由于left指向的是第一个大于或等于基准元素的位置，这次交换确保了基准元素左侧的所有元素都不大于它，而右侧的所有元素都不小于它。
    return left


alist = [54, 26, 93, 26, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
