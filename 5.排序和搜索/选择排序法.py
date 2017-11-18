# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/17 15:19'
"""
选择排序改进了冒泡排序，每次遍历列表只做一次交换。为了做到这一点，一个选择排序在
他遍历时寻找最大的值，并在完成遍历后，将其放置在正确的位置。与冒泡排序一样，在第
一次遍历后，最大的项在正确的地方。 第二遍后，下一个最大的就位。遍历 n-1 次排序 n 个
项，因为最终项必须在第（n-1）次遍历之后。
"""


def selection_sort_max(alist):
    for fillslot in range(len(alist)-1):
        position_of_max = fillslot
        for location in range(fillslot+1, len(alist)):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
        alist[fillslot], alist[position_of_max] = alist[position_of_max], alist[fillslot]

    return alist


def selection_sort_min(alist):
    n = len(alist)
    for i in range(n-1):
        min_set = i
        for j in range(i+1, n):
            if alist[j] < alist[min_set]:
                min_set = j
        alist[i], alist[min_set] = alist[min_set], alist[i]
    return alist


alist=[20,30,40,90,50,60,70,80,100,110]

print(selection_sort_min(alist))
print(selection_sort_max(alist))
