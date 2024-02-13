
def canBeValid(s, locked): 
    stack = list() 
    
    for i in range(len(s)): 
        char = s[i]  
        stack_size = len(stack)
         
        
        if char == "(" :
            if stack_size != 0 and s[stack[stack_size - 1]] == ")" and locked[stack[stack_size - 1]] == '0':
                    stack.pop()  
                    continue
            elif stack_size != 0 and s[stack[stack_size - 1]] == "(" and locked[i] == '0': 
                stack.pop() 
                continue
            
        elif char == ")": 
            
            if stack_size != 0 and s[stack[stack_size - 1]] == "(": 
                stack.pop() 
                continue 
            elif stack_size != 0 and s[stack[stack_size - 1]] == ")" and locked[stack[stack_size - 1]] == '0': 
                stack.pop()  
                continue
        stack.append(i) 
        print(stack)       
    return len(stack) == 0   
    
   


s = "((()(()()))()((()()))))()((()(()"
locked = "10111100100101001110100010001001"


print(canBeValid(s, locked))