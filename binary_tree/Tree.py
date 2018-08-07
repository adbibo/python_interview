#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: Tree.py
# @time: 2018/7/3 下午5:27
# @desc:


class Node(object):
    """节点类"""
    def __init__(self, element=-1, left_child=None, right_child=None):
        self.element = element
        self.left_child = left_child
        self.right_child = right_child


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()
        self.own_queue = []

    def add(self, element):
        """为树添加节点"""
        node = Node(element)
        if self.root.element == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.own_queue.append(self.root)
        else:
            tree_node = self.own_queue[0]  # 此结点的子树还没有齐。
            if tree_node.left_child is None:
                tree_node.left_child = node
                self.own_queue.append(tree_node.left_child)
            else:
                tree_node.right_child = node
                self.own_queue.append(tree_node.right_child)
                self.own_queue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_recursion(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.element)
        self.front_recursion(root.left_child)
        self.front_recursion(root.right_child)

    def middle_recursion(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_recursion(root.left_child)
        print(root.element)
        self.middle_recursion(root.right_child)

    def later_recursion(self, root):
        """利用递归实现树的后序遍历"""
        if root is None:
            return
        self.later_recursion(root.left_child)
        self.later_recursion(root.right_child)
        print(root.element)

    @staticmethod
    def front_stack(root):
        """利用堆栈实现树的先序遍历"""
        if root is None:
            return
        own_stack = []
        node = root
        while node or own_stack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.element)
                own_stack.append(node)
                node = node.left_child
            node = own_stack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right_child  # 开始查看它的右子树

    @staticmethod
    def middle_stack(root):
        """利用堆栈实现树的中序遍历"""
        if root is None:
            return
        own_stack = []
        node = root
        while node or own_stack:
            while node:  # 从根节点开始，一直找它的左子树
                own_stack.append(node)
                node = node.left_child
            node = own_stack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.element)
            node = node.right_child  # 开始查看它的右子树

    @staticmethod
    def later_stack(root):
        """利用堆栈实现树的后序遍历"""
        if root is None:
            return
        own_stack1 = []
        own_stack2 = []
        node = root
        own_stack1.append(node)
        while own_stack1:  # 这个while循环的功能是找出后序遍历的逆序，存在own_stack2里面
            node = own_stack1.pop()
            if node.left_child:
                own_stack1.append(node.left_child)
            if node.right_child:
                own_stack1.append(node.right_child)
            own_stack2.append(node)
        while own_stack2:  # 将own_stack2中的元素出栈，即为后序遍历次序
            print(own_stack2.pop().element)

    @staticmethod
    def level_queue(root):
        """利用队列实现树的层次遍历"""
        if root is None:
            return
        result = list()
        result.append(root.element)
        father_node = [root]
        while len(father_node) > 0:
            child_node = list()
            child_elements = list()
            for node in father_node:
                if node.left_child is not None:
                    child_node.append(node.left_child)
                    child_elements.append(node.element)
                if node.right_child is not None:
                    child_node.append(node.right_child)
                    child_elements.append(node.element)
            father_node = child_node
            if len(child_elements) > 0:
                result.append(child_elements)
        return result

    @staticmethod
    def zhi_shape_queue(root):
        """之字形打印而茶壶"""
        if root is None:
            return
        result = [root]
        current_layer = [root]
        is_even_layer = True
        while len(current_layer) > 0:
            is_even_layer = not is_even_layer
            next_layer = list()
            for node in current_layer:
                if node.left_child is not None:
                    next_layer.append(node.left_child)
                if node.right_child is not None:
                    next_layer.append(node.right_child)
            current_layer = next_layer
            if not current_layer:
                result.extend(current_layer[::-1] if is_even_layer else current_layer)
        return result

    def get_node_num(self, root):
        """二叉树的节点个数"""
        if root is None:
            return 0
        return self.get_node_num(root.left_child) + self.get_node_num(root.right_child) + 1

    def get_depth(self, root):
        """求二叉树的深度"""
        if root is None:
            return 0
        return max(self.get_depth(root.left_child), self.get_depth(root.right_child)) + 1

    def convert(self, root, first_node, ):
        """将二叉查找树变为有序的双向链表"""
        pass

    def get_node_num_k_level(self, root, k):
        """二叉树第K层的节点个数"""
        if root is None or k < 1:
            return 0
        if k == 1:
            return 1
        return self.get_node_num_k_level(root.left_child, k - 1) + self.get_node_num_k_level(root.right_child, k - 1)

    def get_leaf_node_num(self, root):
        """二叉树中叶子节点的个数"""
        if root is None:
            return 0
        if root.left_child is None or root.right_child is None:
            return 1
        return self.get_leaf_node_num(root.left_child) + self.get_leaf_node_num(root.right_child)

    def cmp_tree_structure(self, root1, root2):
        """两棵二叉树是否结构相同"""
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return self.cmp_tree_structure(root1.left_child, root2.right_child) and self.cmp_tree_structure(
            root1.right_child, root2.left_child)

    def tree_is_avl(self, root, height):
        """判断二叉树是不是平衡二叉树"""
        if root is None:
            height = 0
            return True
        left_height = 0
        left_result = self.tree_is_avl(root.left_child, left_height)
        right_height = 0
        right_result = self.tree_is_avl(root.right_child, right_height)
        if left_result and right_result and abs(left_height - right_height) <= 1:
            height = max(left_height, right_height) + 1
            return True
        else:
            height = max(left_height, right_height) + 1
            return False

    def get_mirror(self, root):
        """求二叉树的镜像"""
        if root is None:
            return root
        left = self.get_mirror(root.left_child)
        right = self.get_mirror(root.right_child)
        root.left_child = right
        root.right_child = left
        return root


if __name__ == '__main__':
    """主函数"""
    elements = range(10)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for element in elements:
        tree.add(element)  # 逐个添加树的节点

    # print('队列实现层次遍历:'
    # tree.level_queue(tree.root)
    #
    # print('\n\n递归实现先序遍历:'
    # tree.front_recursion(tree.root)
    # print('\n递归实现中序遍历:'
    # tree.middle_recursion(tree.root)
    # print('\n递归实现后序遍历:'
    # tree.later_recursion(tree.root)

    print('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    # print('\n堆栈实现中序遍历:'
    # tree.middle_stack(tree.root)
    # print('\n堆栈实现后序遍历:'
    # tree.later_stack(tree.root)

    # print('\n\n二叉树中的节点个数'
    # print(tree.get_node_num(tree.root)
    #
    # print('\n\n二叉树中的深度'
    # print(tree.get_depth(tree.root)
    #
    # print('\n\n二叉树第K层的节点个数'
    # print(tree.get_node_num_k_level(tree.root, 3)
    #
    # print('\n\n二叉树中叶子节点的个数'
    # print(tree.get_leaf_node_num(tree.root)
    #
    # print('\n\n判断二叉树是不是平衡二叉树'
    # height = 0
    # print("平衡二叉树" if tree.tree_is_avl(tree.root, height) else "不是平衡二叉树"

    print('\n\n求二叉树的镜像')
    mirror = tree.get_mirror(tree.root)
    print(tree.front_stack(mirror))
