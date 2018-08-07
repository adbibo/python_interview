#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: bit_map.py
# @time: 2018/7/6 下午10:05
# @desc:

# -*- coding: utf-8 -*-
import array

'''''
author: malaka
mail:wengxiaojun1979@gmail.com
city:ShangHai
目的是为了记录url地址，保证不重复抓取url地址;技术实现的概念主要是参考了梁斌的<<走进搜索引擎>>，使用python实现了bitmap
'''


class intBitmap:
    '''''
    说明：保存int大小（4 * 1byte = 4* 8 单位bit）的数据到bitmap中
    len  :是指在每个array对象中要有多少个元素(最好是使用默认的值)

    '''

    def __init__(self, len=8):
        self.len = len
        self.map = array.array('L', '/x00' * self.len * 4)

    def __getitem__(self, id):
        if id > self.len or id < 0:
            print('error! id must >0 and <%i' % self.len)
        else:
            return self.map[id]

    def insert(self, integerI):
        index_Hash = integerI / 32 % self.len
        index_int = integerI % 32
        self.map[index_Hash] = (self.map[index_Hash] | (1 << index_int))

    def __contains__(self, integerI, id=0):
        index_Hash = integerI / 32 % self.len
        index_int = integerI % 32
        if (self.map[index_Hash] & (1 << index_int)):
            return 1
        else:
            return 0


# class MD5BitMap():
#     '''''
#     说明：保存一个md5码到bitmap中 md5码大小（4 * 4byte = 4* 4 * 8 单位bit）的数据到bitmap中，也就是说128个bit
#     size :是指需要生成多少个array对象(最好是使用默认的值)
#     len  :是指在每个array对象中要有多少个元素(最好是使用默认的值)
#
#     '''
#
#     def __init__(self, size=4, len=8):
#         self.size = size
#         self.len = len
#         self.collection = []
#         self.makeCollection()
#
#     def makeCollection(self):
#         for i in range(0, self.size):
#             self.collection.append(array.array('L', '/x00' * self.len * 4))
#
#     def __getitem__(self, id):
#         if id > self.size or id < 0:
#             print('error! id must >0 and <%i' % self.size)
#         else:
#             return self.collection[id]
#
#     def getMd5(self, strURL):
#         import _md5
#         m1 = md5.new()
#         m1.update(strURL)
#         dest1 = m1.hexdigest()
#         print(int(dest1[0:8], 16), int(dest1[8:16], 16), int(dest1[16:24], 16), int(dest1[24:32], 16))
#         return (int(dest1[0:8], 16), int(dest1[8:16], 16), int(dest1[16:24], 16), int(dest1[24:32], 16))
#
#     def insert(self, url):
#         splitUrls = self.getMd5(url)
#         for i in range(0, 4):
#             index_Hash = splitUrls[i] / 32 % 8
#             index_int = splitUrls[i] % 32
#             self.collection[i][index_Hash] = (self.collection[i][index_Hash] | (1 << index_int))
#
#     def __contains__(self, url):
#         splitUrls = self.getMd5(url)
#         for i in range(0, 4):
#             index_Hash = splitUrls[i] / 32 % 8
#             index_int = splitUrls[i] % 32
#             if not (self.collection[i][index_Hash] & (1 << index_int)):
#                 return 0
#         return 1


t = intBitmap()
t.insert(1234)
assert 1234 in t
urlf = 'http://www.gbtai.com/radio369.htm'
# test = MD5BitMap()
# test.insert(urlf)
# assert urlf in test