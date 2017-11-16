# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/15 20:57'


"""
知道我们的基本情况是什么意味着整个算法将分成三个部分：
1. 将原始数字减少为一系列单个位数字。
2. 使用查找将单个位数字数字转换为字符串。
3. 将单个位字符串连接在一起以形成最终结果。
"""


def to_str(n, base):
    convert_string = '0123456789ABCDEF'

    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]


print(to_str(10, 2))