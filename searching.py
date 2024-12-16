from queue import Queue

def search_in_queue(queue, target):
    while not queue.empty():
        item = queue.get()
        if item == target:
            return True
    return False

my_queue = Queue()

my_queue.put(10)
my_queue.put(20)
my_queue.put(30)
my_queue.put(40)

target = 60
is_found = search_in_queue(my_queue, target)

if is_found:
    print(f"{target} found in the queue!")
else:
    print(f"{target} not found in the queue!")
