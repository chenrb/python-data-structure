# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/17 23:25'


def merg(alist):
    mid = len(alist)//2
    if mid <= 0:
        return alist
    else:
        return sorted(merg(alist[:mid]), merg(alist[mid:]))


def sorted(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    while a:
        result.append(a.pop(0))
    while b:
        result.append(b.pop(0))
    return result


def merge_sort(alist):
    print('Splitting ', alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1

    print('Merging ', alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(merg(alist))
merge_sort(alist)