# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/16 9:07'
"""
这里是如何使用中间杆将塔从起始杆移动到目标杆的步骤：
1. 使用目标杆将 height-1 的塔从起始杆移动到中间杆。
2. 将剩余的盘子移动到目标杆。
3. 使用起始杆将 height-1 的塔从中间杆移动到目标杆。
"""


def movedisk(fp, tp):
    print('moving disk from', fp, 'to', tp)


def movetower(height, frompole, topole, withpole):
    if height >= 1:
        movetower(height-1, frompole, withpole, topole)
        movedisk(frompole, topole)
        movetower(height-1, withpole, topole, frompole)


print(movetower(3, 'f', 't', 'w'))