# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/13 10:13'

from pythonds.basic.deque import Deque


def pal_checker(astring):

    chardeque = Deque()

    for ch in astring:
        chardeque.addRear(ch)

    stillequal = True

    while chardeque.size() > 1 and stillequal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillequal = False

    return stillequal


print(pal_checker('asdfgfdsa'))
print(pal_checker('12345654321'))
print(pal_checker('12345555432'))