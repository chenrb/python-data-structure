# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/17 9:57'
"""
冒泡排序需要多次遍历列表。它比较相邻的项并交换那些无序的项。每次遍历列表将下一个
最大的值放在其正确的位置。实质上，每个项“冒泡”到它所属的位置。
"""


def short_bubble_sort1(alist):
    """
    for循环
    :param alist:
    :return:
    """
    passnum = len(alist)
    for i in range(passnum):
        exchanges = False
        for j in range(passnum-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchanges = True
        if not exchanges:
            return alist

    return alist


def short_bubble_sort2(alist):
    """
    while循环
    :param alist:
    :return:
    """
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchanges = True
        passnum -= 1



alist1=[20,30,40,90,50,60,70,80,100,110]
alist2=[20,30,40,90,50,60,70,80,100,110]

short_bubble_sort1(alist1)
short_bubble_sort2(alist2)
print(alist1)
print(alist2)