#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: Solution.py
# @time: 2018/7/5 下午5:33
# @desc: 二叉搜索树与双向链表


class Solution:
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    # 将二叉树转换为有序双向链表
    def covert(self, tree_root):
        if tree_root is None:
            return
        self.covert(tree_root.left)
        if self.list_head is None:
            self.list_head = tree_root
            self.list_tail = tree_root
        else:
            self.list_tail.right = tree_root
            tree_root.left = self.list_tail
            self.list_tail = tree_root
        self.covert(tree_root.right)
        return self.list_head

    # 获得链表的正向序和反向序
    @staticmethod
    def print_list(head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end=" ")
            head = head.left

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def get_bst_with_pre(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = TreeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.get_bst_with_pre(pre[1:order + 1], tin[:order])
                root.right = self.get_bst_with_pre(pre[order + 1:], tin[order + 1:])
                return root


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


if __name__ == '__main__':
    solution = Solution()
    pre_order_seq = [4, 2, 1, 3, 6, 5, 7]
    middle_order_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = solution.get_bst_with_pre(pre_order_seq, middle_order_seq)
    head = solution.covert(treeRoot1)
    solution.print_list(head)
