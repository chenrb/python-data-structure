# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/11 23:04'

"""
假设中缀表达式是一个由空格分隔的标记字符串。 操作符标记是 *，/，+ 和 - ，以及左右括
号。操作数是单字符 A，B，C 等。 以下步骤将后缀顺序生成一个字符串。
1. 创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。
2. 通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。
3. 从左到右扫描标记列表。
    如果标记是操作数，将其附加到输出列表的末尾。
    如果标记是左括号，将其压到 opstack 上。
    如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
    如果标记是运算符， *，/，+ 或 - ，将其压入 opstack。但是，首先删除已经在opstack 中具有更高或相等优先级的任何运算符，
并将它们加到输出列表中。
4. 当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到
输出列表的末尾。
为了在 Python 中编写算法，我们使用一个名为 prec 的字典来保存操作符的优先级。这个字
典将每个运算符映射到一个整数，可以与其他运算符的优先级（我们使用整数3，2和1）进行
比较。左括号将赋予最低的值。这样，与其进行比较的任何运算符将具有更高的优先级，将
被放置在它的顶部。
"""

from pythonds.basic.stack import Stack


def infix_to_postfix(infixexpr):
    """
    中辍转后辍
    :param infixexpr:
    :return:
    """
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()

    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixlist.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return ''.join(postfixlist)


# print(infix_to_postfix('A * B + C * D'))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


"""
后辍表达式计算
假设后缀表达式是一个由空格分隔的标记字符串。 运算符为 *，/，+ 和 - ，操作数假定为单个整数值。 输出将是一个整数结果。
1. 创建一个名为 operandStack 的空栈。
2. 拆分字符串转换为标记列表。
3. 从左到右扫描标记列表。
    如果标记是操作数，将其从字符串转换为整数，并将值压到operandStack。
    如果标记是运算符 *，/，+ 或 - ，它将需要两个操作数。弹出operandStack 两次。
    第一个弹出的是第二个操作数，第二个弹出的是第一个操作数。执行算术运算后，将结果压到操作数栈中。
4. 当输入的表达式被完全处理后，结果就在栈上，弹出 operandStack 并返回值。
用于计算后缀表达式的完整函数见 ActiveCode 2，为了辅助计算，定义了一个函数 doMath,它将获取两个操作数和运算符，执行相应的计算。
"""


def postfix_eval(postfixexpr):
    """
    后缀表达式计算
    :param postfixexpr:
    :return:
    """
    operandstack = Stack()
    tokenlist = postfixexpr.split()

    for token in tokenlist:
        if token in '0123456789':
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = domath(token, operand1, operand2)
            operandstack.push(result)
    return operandstack.pop()


def domath(op, op1, op2):
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2


print(postfix_eval('7 8 + 3 2 + /'))