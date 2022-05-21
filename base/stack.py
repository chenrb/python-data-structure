class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.items)
