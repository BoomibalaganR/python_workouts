
def removeDuplicates(s, k): 
    
    stack = list() 
    
    for char in s: 
        
        if len(stack) == 0:
            stack.append({char: 1}) 
            continue  
        
        stackSize = len(stack) - 1 
        val = stack[stackSize].get(char)
       
        if val is  None: 
            stack.append({char:1}) 
        
        elif val == k-1: 
            stack.pop() 
        
        else: 
            stack[stackSize][char] += 1 
    
    
    res = str()   
    for di in stack:
        res+=list(di.keys())[0] * list(di.values())[0]

    return res

s = "deeedbbcccbdaa" 
k = 4
print(removeDuplicates(s, k))