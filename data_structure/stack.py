#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: stack.py
# @time: 2018/7/15 上午9:45
# @desc:

class OVERFLOW(Exception): pass


class UNDERFLOW(Exception): pass


class Stack(object):
    def __init__(self, size):
        self.top = -1
        self.S = [0 for _ in range(size)]
        self.size = size

    STACK_IS_EMPTY = lambda self: self.top == -1
    STACK_IS_FULL = lambda self: self.top == self.size - 1

    def push(self, data):
        if self.STACK_IS_FULL():
            raise OVERFLOW("stack is full")

        self.top += 1
        self.S[self.top] = data

    def pop(self):
        if self.STACK_IS_EMPTY():
            raise UNDERFLOW("stack is empty")
        x = self.S[self.top]
        self.top -= 1
        return x
