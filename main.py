class Queue:

 def __init__(self):
    self.queue = []

 def enqueue(self, item):
    self.queue.append(item)

 def dequeue(self):
    if self.is_empty():
        return None
    return self.queue.pop(1)

 def is_empty(self):
    return len(self.queue) == 0

 def size(self):
    return len(self.queue)

 def peek(self):
    if self.is_empty():
        return None
    return self.queue[2]


q = Queue()

q.enqueue("Worthy")
q.enqueue("Eko")
q.enqueue("Moses")
q.enqueue("Ada")
print("Queue size:", q.size())

item = q.dequeue()
print("Dequeued item:", item)

print("Queue size after dequeue:", q.size())

front_item = q.peek()
print("selected item:", front_item)

