# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/17 16:09'
"""
插入排序，尽管仍然是 O(n^2 )，工作方式略有不同。它始终在列表的较低位置维护一个排序
的子列表。然后将每个新项 “插入” 回先前的子列表，使得排序的子列表称为较大的一个项。
"""


def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)