# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/16 21:03'

"""
有序列表对于我们的比较是很有用的。在顺序查找中，当我们与第一个项进行比较时，如果
第一个项不是我们要查找的，则最多还有 n-1 个项目。 二分查找从中间项开始，而不是按
顺序查找列表。 如果该项是我们正在寻找的项，我们就完成了查找。 如果它不是，我们可以
使用列表的有序性质来消除剩余项的一半。如果我们正在查找的项大于中间项，就可以消除
中间项以及比中间项小的一半元素。
二分法查找的时间复杂度为O( log^n )
"""


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while not found and first <= last:
        midpoint = (first + last) // 2
        if item == alist[midpoint]:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def b_search(alist, item):
    """
    使用递归
    :param alist:
    :param item:
    :return:
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return b_search(alist[:midpoint], item)
            else:
                return b_search(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
print(b_search(testlist, 3))
print(b_search(testlist, 13))