def create_stack():
    return []

def push(stack, item):
    stack.append(item)
    print(f"Pushed item: {item}")

def pop(stack):
    if len(stack) == 0: return "Stack is empty"
    return stack.pop()

stack = create_stack()
while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push  2. Pop  3. Display  4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter element to push: ")
        push(stack, val)
    elif choice == '2':
        print("Popped item:", pop(stack))
    elif choice == '3':
        print("Current Stack:", stack)
    elif choice == '4':
        break
