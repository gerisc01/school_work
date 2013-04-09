# a class for making queues
# methods - adding, removing, finding if it's empty, size of queue
# front of the list is the back of the queue
class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, theitem):
        self.items.insert(0, theitem)
    def dequeue(self):
        return self.items.pop()
        
