# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/13 10:13'

from base.deque import Deque


def pal_checker(astring):

    chardeque = Deque()

    for ch in astring:
        chardeque.add_rear(ch)

    stillequal = True

    while chardeque.size() > 1 and stillequal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if first != last:
            stillequal = False

    return stillequal


print(pal_checker('asdfgfdsa'))
print(pal_checker('12345654321'))
print(pal_checker('12345555432'))