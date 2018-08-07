#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: link_list_sort.py
# @time: 2018/7/4 下午10:48
# @desc:
from random import randint

class Node:
    def __init__(self, x, next_node=None):
        self.data = x
        self.next = next_node


class ListNode:
    def __init__(self):
        self.root = None
        self.size = 0

    def add_node(self, data):
        """添加节点"""
        if self.root is None:
            self.root = Node(data, None)
        else:
            head = self.root
            while head.next:
                head = head.next
            head.next = Node(data, None)
        self.size += 1
        return self.root

    def append(self, data):
        """添加节点至尾部"""
        self.add_node(data)

    def front_append(self, data):
        """添加节点至头部"""
        if self.root is None:
            self.root = Node(data)
        else:
            head = Node(data)
            head.next = self.root
            self.root = head
        self.size += 1

    def insert_node(self, data, index):
        """在指定位置插入节点"""
        if self.root is None:
            return
        if index <= 0 or index > self.size:
            return
        elif index == 1:
            self.front_append(data)
        elif index == self.size + 1:
            self.append(data)
        else:
            cnt = 2
            head = self.root
            head_next = self.root.next
            while head_next:
                if cnt == index:
                    tmp = Node(data)
                    head.next = tmp
                    tmp.next = head_next
                    break
                else:
                    head = head.next
                    cnt += 1
                    head_next = head_next.next
            self.size += 1
            self.root = head

    def delete_node(self, index):
        """删除制定位置节点"""
        if self.root is Node:
            return
        if index <= 0 or index > self.size:
            return
        if index == 1:
            self.root = self.root.next
        else:
            head = self.root
            head_next = self.root.next
            cnt = 2
            while head_next:
                if index == cnt:
                    head.next = head_next.next
                    self.size -= 1
                else:
                    head = head.next
                    head_next = head_next.next
                    cnt += 1

    def is_empty(self):
        """判断链表是否为空"""
        return not self.root or not self.size

    def truncate(self):
        """清空链表"""
        if not self.root or not self.size:
            return
        else:
            head = self.root
            while head:
                head.data = None
                head = head.next
            self.root = None
            self.size = 0
            head = None

    def get_data(self, index):
        """获取制定位置的节点值"""
        if not self.root or not self.size:
            return None
        if index <= 0 or index > self.size:
            return None
        else:
            cnt = 1
            head = self.root
            while head:
                if index == cnt:
                    return head.data
                else:
                    cnt += 1
                    head = head.next

    def peek(self):
        """获取尾节点值"""
        return self.get_data(self.size)

    def pop(self):
        """删除尾节点,并返回节点值"""
        if not self.root or not self.size:
            return None
        elif self.size == 1:
            top = self.root.data
            self.root = None
            return top
        else:
            pre = self.root
            cursor = pre.next
            while cursor.next is not None:
                pre = cursor
                cursor = cursor.next
            top = cursor.data
            cursor = None
            pre.next = None
            return top

    def reverse(self):
        """单链表逆序实现"""
        if self.root is None:
            return
        if self.size == 1:
            return
        else:
            post = None
            pre = None
            cursor = self.root
            while cursor is not None:
                # print('逆序操作逆序操作')
                post = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = post
            self.root = pre

    def delete_duplicate(self):
        """删除链表中的重复元素"""
        # 使用一个map来存放即可，类似于变形的“桶排序”
        dic = {}
        if self.root is None:
            return
        if self.size == 1:
            return
        pre = self.root
        cursor = pre.next
        dic = {}
        # 为字典赋值
        temp = self.root
        while temp is not None:
            dic[str(temp.data)] = 0
            temp = temp.next
        temp = None
        # 开始实施删除重复元素的操作
        while cursor is not None:
            if dic[str(cursor.data)] == 1:
                pre.next = cursor.next
                cursor = cursor.next
            else:
                dic[str(cursor.data)] += 1
                pre = cursor
                cursor = cursor.next

    def update_node(self, index, dataue):
        """修改指定位置节点的值"""
        if self.root is None:
            return
        if index < 0 or index > self.size:
            return
        if index == 1:
            self.root.data = dataue
            return
        else:
            cursor = self.root.next
            counter = 2
            while cursor is not None:
                if counter == index:
                    cursor.data = dataue
                    break
                cursor = cursor.next
                counter += 1

    def size(self):
        """获取单链表的大小"""
        counter = 0
        if self.root is None:
            return counter
        else:
            cursor = self.root
            while cursor is not None:
                counter += 1
                cursor = cursor.next
            return counter

    # 打印链表自身元素
    def list_print(self):
        if self.root is None:
            return
        else:
            cursor = self.root
            while cursor is not None:
                print(cursor.data, end='\t')
                cursor = cursor.next
            print()


if __name__ == '__main__':
    # 创建一个链表对象
    linked_list = ListNode()
    # 判断当前链表是否为空
    print("链表为空%d" % linked_list.is_empty())
    # 判断当前链表是否为空
    linked_list.add_node(1)
    print("链表为空%d" % linked_list.is_empty())
    for _ in range(10):
        value = randint(1, 99)
    # 添加一些节点，方便操作
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    linked_list.add_node(6)
    linked_list.add_node(5)
    linked_list.add_node(6)
    linked_list.add_node(7)
    linked_list.add_node(3)
    # 打印当前链表所有值
    print('打印当前链表所有值')
    linked_list.list_print()
    # 测试对链表求size的操作
    print("链表的size: " + str(linked_list.size))
    # 测试指定位置节点值的获取
    print('测试指定位置节点值的获取')
    print(linked_list.get_data(1))
    print(linked_list.get_data(linked_list.size))
    print(linked_list.get_data(7))
    # 测试删除链表中指定值， 可重复性删除
    print('测试删除链表中指定值， 可重复性删除')
    linked_list.delete_node(4)
    linked_list.list_print()
    linked_list.delete_node(3)
    linked_list.list_print()
    # 去除链表中的重复元素
    print('去除链表中的重复元素')
    linked_list.delete_duplicate()
    linked_list.list_print()
    # 指定位置的链表元素的更新测试
    print('指定位置的链表元素的更新测试')
    linked_list.update_node(6, 99)
    linked_list.list_print()
    # 测试在链表首部添加节点
    print('测试在链表首部添加节点')
    linked_list.front_append(77)
    linked_list.front_append(108)
    linked_list.list_print()
    # 测试在链表尾部添加节点
    print('测试在链表尾部添加节点')
    linked_list.append(99)
    linked_list.append(100)
    linked_list.list_print()
    # 测试指定下标的插入操作
    print('测试指定下标的插入操作')
    linked_list.insert_node(1, 10010)
    linked_list.insert_node(3, 333)
    linked_list.insert_node(linked_list.size, 99999)
    linked_list.list_print()
    # 测试peek 操作
    print('测试peek 操作')
    print(linked_list.peek())
    linked_list.list_print()
    # 测试pop 操作
    print('测试pop 操作')
    print(linked_list.pop())
    linked_list.list_print()
    # 测试单链表的逆序输出
    print('测试单链表的逆序输出')
    linked_list.reverse()
    linked_list.list_print()
    # 测试链表的truncate操作
    print('测试链表的truncate操作')
    linked_list.truncate()
    linked_list.list_print()
