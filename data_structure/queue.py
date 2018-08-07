#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: queue.py
# @time: 2018/7/15 上午9:55
# @desc:


class UNDERFLOW(Exception): pass  # 下溢


class OVERFLOW(Exception): pass  # 上溢


class Queue(object):
    def __init__(self, size):
        self.head = self.tail = 0
        self.S = [0 for _ in range(0, size)]
        self.size = size

    # 判断队列是否已满
    QUEUE_FULL = lambda self: self.head == (self.tail + 1) % self.size
    # 判断队列是否为空
    QUEUE_EMPTY = lambda self: self.head == self.tail

    # 入队
    def ENQUEUE(self, x):
        if self.QUEUE_FULL(): raise OVERFLOW("the queue is full")
        self.S[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    # 出队
    def DEQUEUE(self):
        if self.QUEUE_EMPTY(): raise UNDERFLOW("the queue is empty")
        x = self.S[self.head]
        self.head = (self.head + 1) % self.size
        return x


