#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: transposition.py
# @time: 2018/7/9 下午3:46
# @desc:


def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    if not A:
        return
    row = 0
    result = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    while row < len(A):
        for col in range(0, len(A[0])):
            result[col][row] = A[row][col]
        row += 1
    return result


test_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_array)
print(transpose(test_array))

test_array2 = [[1, 2, 3], [4, 5, 6]]
print(test_array2)
print(transpose(test_array2))
