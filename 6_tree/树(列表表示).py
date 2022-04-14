# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/18 21:06'


mytree = ['a',
    ['b',
     ['d', [], []], ['e', [], []]],
    ['c',
     ['f', [], []], []]
]


print(mytree)
print('left subtree = ', mytree[1])
print('root = ', mytree[0])
print('right subtree = ', mytree[2])


tre = ['a',
    ['b', []],
    ['c', []]
]


def binary_tree(r):
    return [r, [], []]


def insert_left(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root


def insert_right(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, newval):
    root[0] = newval


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# root = binary_tree(tre)
print(mytree)
print(insert_left(mytree, ['a']))
print(insert_right(mytree, ['a']))
print(get_left_child(mytree))
print(get_right_child(mytree))