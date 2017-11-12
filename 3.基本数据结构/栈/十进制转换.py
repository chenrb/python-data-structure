# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/11 21:33'
from pythonds.basic.stack import Stack


def divide_by2(decNumber):
    """
    十进制转二进制
    :param decNumber:
    :return:
    """
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring


def base_converter(decNumber, base):
    """
    十进制转其他进制
    :param decNumber:
    :param base:
    :return:
    """
    remstack = Stack()
    digits = '0123456789ABCDEF'

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newstring = ''
    while not remstack.isEmpty():
        newstring = newstring + digits[remstack.pop()]

    return newstring

