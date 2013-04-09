#Scott Gerike CS151
#2/15/2010
#A Class that works with stacks
#methods: isEmpty, size, push, pop
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    
