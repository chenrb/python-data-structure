# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/15 21:17'

import turtle


my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def draw_sporal(my_turtle, linelen):
    if linelen > 0:
        my_turtle.forward(linelen)
        my_turtle.right(90)
        draw_sporal(my_turtle, linelen-5)


# draw_sporal(my_turtle, 100)
# my_win.exitonclick()


def tree(branchlen, t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15, t)
        t.left(40)
        tree(branchlen-15, t)
        t.right(20)
        t.backward(branchlen)


def main():
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    mywin.exitonclick()


main()