def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued item: {item}")

def dequeue(queue):
    if len(queue) == 0: return "Queue is empty"
    return queue.pop(0) #

queue = []
while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue  2. Dequeue  3. Display  4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter element to enqueue: ")
        enqueue(queue, val)
    elif choice == '2':
        print("Dequeued item:", dequeue(queue))
    elif choice == '3':
        print("Current Queue:", queue)
    elif choice == '4':
        break
