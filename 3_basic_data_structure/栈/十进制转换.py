# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/11 21:33'

from base import Stack


def divide(dec, base):
    s = Stack()
    digits = '0123456789ABCDEF'

    while dec > 0:
        dec, tmp = divmod(dec, base)
        s.push(tmp)

    ret = ''
    while not s.is_empty():
        ret += digits[s.pop()]
    return ret


print(divide(10, 2))