def removeDuplicate(s, k): 
    
    stack = list()
    
    for char in s:  
        
        if len(stack) != 0 and stack[len(stack)-1]  and stack[len(stack)-1].get(char) == k-1: 
            stack.pop() 
        else:
            stack.append({char: 1})        
        print(stack[len(stack)-1])
    print(stack)

s = "deeedbbcccbdaa"
k = 3 

removeDuplicate(s, k)