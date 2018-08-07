#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: two_sum_sorted_array.py
# @time: 2018/7/9 下午5:27
# @desc:
"""
给定一个有序数组和一个目标值, 数组中取出两个数之和为目标值, 输出这两个数的下标
"""


def two_sum1(array, target):
    result = list()
    index_dict = dict()
    for index in range(len(array)):
        sub_result = target - array[index]
        if sub_result not in index_dict:
            index_dict[array[index]] = index
        else:
            result.append([index_dict[sub_result], index])

    return result


def two_sum2(array, target):
    result = list()
    for index in range(len(array)):
        for sub_index in range(index + 1, len(array)):
            if array[index] + array[sub_index] == target:
                result.append([index, sub_index])

    return result


def two_sum3(array, target):
    result = list()
    first_index = 0
    last_index = len(array) - 1
    while first_index < last_index:
        res = array[first_index] + array[last_index]
        if res == target:
            result.append([first_index, last_index])
            first_index += 1
        elif res > target:
            last_index -= 1
        else:
            first_index += 1
    return result


if __name__ == '__main__':
    array = [-3, -2, -1, 1, 3, 5, 6, 8, 11, 14]
    target = 0
    print(two_sum1(array, target))
    print(two_sum2(array, target))
    print(two_sum3(array, target))
