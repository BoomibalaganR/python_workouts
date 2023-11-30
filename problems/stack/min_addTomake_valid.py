
def minAddToMakeValid(s):
    
    stack = list() 
    count = 0
    for c in s:
        
        if c == "(":
            stack.append(c)
            continue 
        if len(stack) != 0 and stack[len(stack)-1] == "(":
            stack.pop() 
        else:
            count+=1
    
    if len(stack) != 0: 
        count+=len(stack) 
    return count
    

s = ")(((" 

print("min add count: ",minAddToMakeValid(s))