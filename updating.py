from queue import Queue

q = Queue()

q.put("Worthy")
q.put("Eko")
q.put("Adidas")


print("Before update:", list(q.queue))

q.queue[1] = "Moses"

print("After update:", list(q.queue))
