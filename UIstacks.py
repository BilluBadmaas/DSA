# Creating a stack
def create_stack():
    stack = []
    return stack
stack = create_stack()

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0
x = check_empty(stack)
print(x)

# Adding items into stack
def push(stack, item):
    stack.append(item)
    print("Pushed Item: " + item)

# ✅ Only change — replace hardcoded pushes with user input loop
n = int(input("How many items to push? "))
for i in range(n):
    item = input("Enter item: ")
    push(stack, item)

print(stack)

# Removing an element from stack
def pop(stack):
    if(check_empty(stack)):
        return "Stack is Empty!!"
    return stack.pop()

print("Popped Item: " + pop(stack))