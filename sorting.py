from queue import Queue


def sort_queue(queue):

    elements = []
    while not queue.empty():
        elements.append(queue.get())

    sorted_elements = sorted(elements)

    for element in sorted_elements:
        queue.put(element)


q = Queue()

q.put(5)
q.put(2)
q.put(7)
q.put(1)
q.put(9)
print("Queue before sorting:", list(q.queue))

sort_queue(q)
print("Queue after sorting:", list(q.queue))

#Sorting in Python is arranging the data in a particular format or order.
# The sorting can be both ascending and descending of data elements