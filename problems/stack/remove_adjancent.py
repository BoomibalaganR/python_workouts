
def removeDuplicate(s: str) -> str:
    
    stack = list() 
    
    for char in s:
        
        if len(stack) != 0 and stack[len(stack) - 1] == char:
            stack.pop() 
            continue 
        stack.append(char)

    return "".join(stack)



s = "abbaca" 
print(removeDuplicate(s))