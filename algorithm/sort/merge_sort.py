# /usr/bin/env python
# -*- coding=utf-8 -*-

"""
归并排序

归并排序也称合并排序，是分治法的典型应用。分治思想是将每个问题分解成个个小问题，将每个小问题解决，然后合并。

具体的归并排序就是，将一组无序数按n/2递归分解成只有一个元素的子项，一个元素就是已经排好序的了。然后将这些有序的子元素进行合并。

合并的过程就是 对 两个已经排好序的子序列，先选取两个子序列中最小的元素进行比较，选取两个元素中最小的那个子序列并将其从子序列中

去掉添加到最终的结果集中，直到两个子序列归并完成。
"""


def merge(left_nums, right_nums):
    """ merge """
    # 切片边界,左闭右开并且是了0为开始  
    result = list()
    l = r = 0
    while l < len(left_nums) and r < len(right_nums):
        if left_nums[l] < right_nums[r]:
            result.append(left_nums[l])
            l += 1
        else:
            result.append(right_nums[r])
            r += 1
    if l < len(left_nums):
        result.extend(left_nums[l:])
    if r < len(right_nums):
        result.extend(right_nums[r:])
    return result


def merge_sort(nums):
    """ merge sort
    merge_sort函数中传递的是下标，不是元素个数
    """
    if len(nums) <= 1:
        return nums
    middle = int(len(nums) / 2)
    left_nums = merge_sort(nums[:middle])
    right_nums = merge_sort(nums[middle:])
    return merge(left_nums, right_nums)


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is:', nums)
    # merge_sort(nums)
    print('merge sort:', merge_sort(nums))
