# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/11 20:56'

"""
从空栈开始，从左到右处理括号字符串。如果一个符号是一个开始符号，将其作为一个信号，
对应的结束符号稍后会出现。另一方面，如果符号是结束符号，弹出栈，只要弹出栈的开始
符号可以匹配每个结束符号，则括号保持匹配状态。如果任何时候栈上没有出现符合开始符
号的结束符号，则字符串不匹配。最后，当所有符号都被处理后，栈应该是空的。
"""
from base import Stack


def par_checker_one(symbol_string):
    """
    单个'('检验
    :param symbol_string:
    :return:
    """
    s = Stack()
    balance = True

    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
                break
            else:
                s.pop()

    if balance and s.is_empty():
        return True
    else:
        return False


def par_checker(symbol_string):
    """
    '([{'检验
    :param symbol_string:
    :return:
    """
    s = Stack()
    balance = True

    for symbol in symbol_string:
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
                break
            tmp = s.peek()
            if matched(tmp, symbol):
                s.pop()
            else:
                balance = False
                break

    if balance and s.is_empty():
        return True
    else:
        return False


def matched(left, right):
    opens = '([{'
    closes = ')]}'
    return opens.index(left) == closes.index(right)


print(par_checker('(([[))]]'))
print(par_checker('(([[]]))'))
print(par_checker('({(([[]]))})'))
print(par_checker('((((()))))'))
print(par_checker('(()'))
