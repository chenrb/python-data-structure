# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/17 23:02'


"""
希尔排序（有时称为“递减递增排序”）通过将原始列表分解为多个较小的子列表来改进插入排
序，每个子列表使用插入排序进行排序。 选择这些子列表的方式是希尔排序的关键。不是将
列表拆分为连续项的子列表，希尔排序使用增量i（有时称为 gap ），通过选择 i 个项的所有
项来创建子列表。
"""


def shell_sort(alist):
    sublistcount = len(alist)//2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)

        print('After increments of size ', sublistcount, 'The list is ', alist)

        sublistcount = sublistcount//2


def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)