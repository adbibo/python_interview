#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: two_dim_array.py
# @time: 2018/7/7 下午9:19
# @desc: N*N的数组，行有序（从小到大），列有序（从小到大），找到第k大的数字
# 比如：这是个3*3的数组，找到里面第四大的数字
# 1, 2, 6，
# 5, 7, 9,
# 11,13,19


def cnt_low(array, m, n, mid):
    cnt = 0
    x = n - 1
    y = 0
    while x > 0 and y <= m - 1:
        while x >= 0 and array[y][x] > mid:
            x -= 1
        if x < 0:
            break
        cnt += x + 1
        y += 1
    return cnt


def find_two_dim_array_kth(array, k):
    m = len(array)
    if m == 0:
        return 0
    n = len(array[0])
    if n == 0:
        return 0
    min_val = array[0][0]
    max_val = array[m - 1][n - 1]

    while min_val < max_val:
        mid = (max_val + min_val) / 2 + min_val
        cnt = cnt_low(array, m, n, mid)
        if cnt < k:
            min_val = mid
        else:
            max_val = mid
    if cnt_low(array, m, n, min_val) >= k:
        return min_val
    return max_val


if __name__ == '__main__':
    test_nums = [[1, 2, 6], [5, 7, 9], [11, 13, 19]]
    # print(test_nums)

    print(find_two_dim_array_kth(test_nums, 2))
