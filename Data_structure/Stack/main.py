from stack import Stack

stack = Stack(2)  

stack.push(1)
stack.push(2)  

stack.push(3)
stack.display() 

print("\npeek element: ",stack.peek()) 

print("popped element: ",stack.pop()) 
print("popped element: ",stack.pop()) 
print("popped element: ",stack.pop()) 
