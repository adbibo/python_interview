# !/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: select_sort.py
# @time: 2018/7/4 下午5:30
# @desc:
from random import randint


def select_sort(array):
    len_array = len(array)
    for index1 in range(len_array):
        array_min = index1
        for index2 in range(index1 + 1, len_array):
            if array[index2] < array[array_min]:
                array_min = index2
        array[index1], array[array_min] = array[array_min], array[index1]


if __name__ == '__main__':
    array = list(set([randint(1, 100) for _ in range(15)]))
    print(array)
    select_sort(array)
    print(array)
