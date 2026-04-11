# Creating a Queue
def create_queue():
    queue = []
    return queue
queue = create_queue()

# Check if queue is empty
def is_empty(queue):
    return len(queue) == 0
y = is_empty(queue)
print(y)

# Add elements to Queue (Enqueue)
def enqueue(queue, item):
    queue.append(item)
    print("Enqueued: ", item)

# ✅ Only change — replace hardcoded enqueues with user input loop
n = int(input("How many items to enqueue? "))
for i in range(n):
    item = input("Enter item: ")
    enqueue(queue, item)

print("Queue: ", queue)

# Remove element from Queue (Dequeue)
def deque(queue):
    if is_empty(queue):
        return "Queue is Empty!!!"
    return queue.pop(0)

print("Dequeued: ", deque(queue))
print("Dequeued: ", deque(queue))
print("Current Queue: ", queue)