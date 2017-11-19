# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/18 22:27'


class binary_tree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, newnode):
        if self.leftchild is None:
            self.leftchild = binary_tree(newnode)
        else:
            t = binary_tree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, newnode):
        if self.rightchild is None:
            self.rightchild = binary_tree(newnode)
        else:
            t = binary_tree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setrootval(self, obj):
        self.key = obj

    def getrootval(self):
        return self.key


r = binary_tree('a')
print(r.getrootval())
print(r.getleftchild())
print(r.getleftchild())
r.insertleft('b')
print(r.getleftchild())
print(r.getleftchild().getrootval())
r.insertright('c')
print(r.getrightchild())
print(r.getrightchild().getrootval())
r.getrightchild().setrootval('hello')
print(r.getrightchild().getrootval())