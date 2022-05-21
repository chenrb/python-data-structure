# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/11 15:51'

"""

乱序字符串问题
利用两个乱序字符串具有相同数目的 a, b, c 等字符的事实。我们首先计算的是每个字母出现的次数。
由于有 26 个可能的字符，我们就用 一个长度为 26 的列表，每个可能的字符占一个位置。
每次看到一个特定的字符，就增加该位置的计数器。最后如果两个列表的计数器一样，则字符串为乱序字符串。

算法分析是一种独立的测量算法的方法。
大O表示法允许根据问题的大小，通过其主要部分来对算法进行分类。

"""
from utils import time_decorator


@time_decorator
def anagram_solution(s1, s2):
    c1, c2 = [0] * 26, [0] * 26

    base = ord('a')

    for i in range(len(s1)):
        pos = ord(s1[i]) - base
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - base
        c2[pos] = c2[pos] + 1

    j = 0
    stillok = True
    while stillok and j < 26:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillok = False

    return stillok


print(anagram_solution('apple', 'pplea'))


class Single(object):
    instance = {}

    def __new__(cls, *args, **kwargs):
        if not Single.instance:
            inst = super().__new__(cls, *args, **kwargs)
            Single.instance[inst] = inst
        return Single.instance[inst]
