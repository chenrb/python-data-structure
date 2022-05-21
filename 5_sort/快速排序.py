# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/18 10:00'


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


def quick(lis, left, right):
    if left >= right:
        return lis

    flag = lis[left]
    i = left
    j = right

    while left < right:
        while left < right and lis[right] >= flag:
            right -= 1
        lis[left] = lis[right]
        while left < right and lis[left] <= flag:
            left += 1
        lis[right] = lis[left]
    lis[right] = flag
    quick(lis, i, left - 1)
    quick(lis, left + 1, j)
    return lis


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# quick_sort(alist)
quick(alist, 0, len(alist)-1)
print(alist)
