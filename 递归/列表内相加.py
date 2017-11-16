# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/15 20:41'


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


print(listsum([1, 2, 3, 4, 5]))