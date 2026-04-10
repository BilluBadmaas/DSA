#creating a stack
def create_stack():
   stack=[]
   return stack
#creating an empty stack
def check_empty(stack):
   return len(stack)==0
#adding items into the stack
def push(stack,item):
   stack.append(item)
   print("pushed item:"+item)
#removing an ele from the stack
def pop(stack):
    if (check_empty(stack)):
      return "stack is empty"
    return stack.pop()
#callimg the fxn
stack=create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("poped item: "+pop(stack))
