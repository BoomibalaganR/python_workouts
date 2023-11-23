
def removeStar(s: str) -> str:
    
    stack = list() 
    res = str() 
    
    for c in s:
      
        if c == "*" and len(stack) != 0: 
          stack.pop()  
          
        else:
            stack.append(c)
    
    return res.join(stack)
      




s = "leet**cod*e" 
res = removeStar(s) 

print("removed star: ",res)