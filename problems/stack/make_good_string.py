def makeGood(s: str) -> str: 
    
    stack = list()
    for char in s:
        
        if len(stack) != 0 and char.islower() and stack[len(stack) - 1] == char.upper():
            stack.pop() 
            continue    
        
        if len(stack) != 0 and char.isupper() and stack[len(stack) - 1] == char.lower():
            stack.pop() 
            continue  
        
        stack.append(char)

    return "".join(stack) 

s = "leEeetcode"  

print(makeGood(s))