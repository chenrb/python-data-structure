# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/12 21:00'
"""
队列的典型应用之一是模拟需要以 FIFO 方式管理数据的真实场景。首先，让我们看看孩子们
的游戏烫手山芋，在这个游戏中（见 Figure 2），孩子们围成一个圈，并尽可能快的将一个
山芋递给旁边的孩子。在某一个时间，动作结束，有山芋的孩子从圈中移除。游戏继续开始
直到剩下最后一个孩子。
"""

from pythonds.basic.queue import Queue


def hot_potato(namelist, num):
    """
    模拟烫手山芋
    :param namelist:
    :param num:
    :return:
    """
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 2))