# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/19 11:08'
"""
1、如果当前符号是 '(' ，添加一个新节点作为当前节点的左子节点，并下降到左子节点。
2、如果当前符号在列表 ['+'，' - '，'/'，'*'] 中，请将当前节点的根值设置为由当前符号表示的运算符。 
    添加一个新节点作为当前节点的右子节点，并下降到右子节点。
3、如果当前符号是数字，请将当前节点的根值设置为该数字并返回到父节点。
4、如果当前令牌是 ')' ，则转到当前节点的父节点。
"""

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator


def buildparsetree(fpexp):
    fplist = fpexp.split()
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    currenttree = etree
    for i in fplist:
        if i == '(':
            currenttree.insertLeft('')
            pstack.push(currenttree)
            currenttree = currenttree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currenttree.setRootVal(int(i))
            parent = pstack.pop()
            currenttree = parent
        elif i in ['+', '-', '*', '/']:
            currenttree.setRootVal(i)
            currenttree.insertRight('')
            pstack.push(currenttree)
            currenttree = currenttree.getRightChild()
        elif i == ')':
            parent = pstack.pop()
            currenttree = parent
        else:
            raise ValueError
    return etree


def evaluate(parsetree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    leftc = parsetree.getLeftChild()
    rightc = parsetree.getRightChild()

    if leftc and rightc:
        fn = opers[parsetree.getRootVal()]
        return fn(evaluate(leftc), evaluate(rightc))
    else:
        return parsetree.getRootVal()


def preorder(tree):
    """
    前序遍历
    :param tree:
    :return:
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    """
    后序遍历
    :param tree:
    :return:
    """
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    """
    中序遍历
    :param tree:
    :return:
    """
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postordereval(tree):
    """
    后续遍历计算树
    :param tree:
    :return:
    """
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def printexp(tree):
    """
    返回完全括号式
    :param tree:
    :return:
    """
    sval = ''
    if tree:
        sval = '(' + printexp(tree.getLeftChild())
        sval = sval + str(tree.getRootVal())
        sval = sval + printexp(tree.getRightChild()) + ')'
    return sval


pt = buildparsetree("( ( 10 + 5 ) * 3 )")
print(postordereval(pt))
print(printexp(pt))
# pt.postorder()
# print(pt)
# print(evaluate(pt))
# print('前序遍历')
# preorder(pt)
# print('后序遍历')
# postorder(pt)
# print('中序遍历')
# inorder(pt)