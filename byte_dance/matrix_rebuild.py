#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: matrix_rebuild.py
# @time: 2018/7/9 下午4:32
# @desc:
"""
给定一个二维数组,如下
[
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32]
]
要求输出一个新的二维数组
[
    [10, 20, 30],
    [10, 21, 30],
    [10, 22, 30],
    [10, 20, 31],
    [10, 21, 31],
    [10, 22, 31],
    [10, 20, 32],
    [10, 21, 32],
    [10, 22, 32],
    [11, 20, 30],
    [11, 21, 30],
    [11, 22, 30],
    [11, 20, 31],
    [11, 21, 31],
    [11, 22, 31],
    [11, 20, 32],
    [11, 21, 32],
    [11, 22, 32],
    [12, 20, 30],
    [12, 21, 30],
    [12, 22, 30],
    [12, 20, 31],
    [12, 21, 31],
    [12, 22, 31],
    [12, 20, 32],
    [12, 21, 32],
    [12, 22, 32],
]
输出的数组为从原数组中每行中取出一个元素组成新的行数据. 二维数组为N*N形式
"""


def matrix_rebuild(A):
    current_result = [[tmp] for tmp in A[0]]
    layer = 1

    while layer < len(A):
        tmp = list()
        for last in current_result:
            for cur in A[layer]:
                tmp.append(last + [cur])
        current_result = tmp
        layer += 1

    return current_result


A = [[x+y for y in range(3)] for x in range(10, 40, 10)]
print(A)

print(matrix_rebuild(A))
