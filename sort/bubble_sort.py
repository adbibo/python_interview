#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: bubble_sort.py
# @time: 2018/7/4 下午5:22
# @desc:

from random import randint


def bubble_sort(array):
    if not array:
        return None
    len_array = len(array)
    for index1 in range(len_array-1):
        for index2 in range(index1, len_array):
            if array[index1] > array[index2]:
                array[index1], array[index2] = array[index2], array[index1]


if __name__ == '__main__':
    array = list(set([randint(1, 100) for _ in range(15)]))
    print(array)

    bubble_sort(array)

    print(array)