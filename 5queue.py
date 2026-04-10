# Creating a Queue
def create_queue():
    queue = []
    return queue
# Creating an Empty Queue
def check_empty(queue):
    return len(queue) == 0
# Adding Items into the Queue (Enqueue)
def enqueue(queue, item):
    queue.append(item)
    print("enqueued item: " + item)
# Removing an Element from the Queue (Dequeue)
def dequeue(queue):
    if (check_empty(queue)):
        return "queue is empty"
    return queue.pop(0)
# Calling the Function
queue = create_queue()
enqueue(queue, str(1))
enqueue(queue, str(2))
enqueue(queue, str(3))
enqueue(queue, str(4))
print("dequeued item: " + dequeue(queue))
