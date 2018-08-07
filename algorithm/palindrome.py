#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 判断数字是不是回文


def is_palindrome(n):
    n = str(n)
    m = n[::-1]
    return n == m


def is_palindrome2(num):
    num = str(num)
    first = 0
    last = len(num) - 1
    while first < last:
        if num[first] == num[last]:
            first += 1
            last -= 1
        else:
            return False
    return True


print(is_palindrome('aba'))

print(is_palindrome2(123432))
