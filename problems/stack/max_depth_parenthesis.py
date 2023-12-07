
def maxDepth(s): 
    count = 0 
    maxi = 0 
    
    stack = list()
    for char in s:
        
        if char == "(":
            stack.append(char)   
                        
        elif char == ")" and len(stack) != 0:  
            maxi =  max(maxi, len(stack) ) 
            stack.pop() 
            
    return maxi


s = "8*((1*(5+6))*(8/6)()(((()))))" 
print("maximum Depth :",maxDepth(s))