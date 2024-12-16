def merge_queues(queue1, queue2):
    merged_queue = []

    while queue1:
        element = queue1.pop(0)
        merged_queue.append(element)

    while queue2:
        element = queue2.pop(0)
        merged_queue.append(element)
    return merged_queue


q1 = [1, 2, 3, 4, 5]
q2 = ['a', 'b', 'c']

merged_q = merge_queues(q1, q2)

for item in merged_q:
    print(item)
