
def removeOuterParentheses(s):
    
    stack = list()   
    res = str() 
    
    for i in range(len(s)):
        
        if s[i] == "(":
            stack.append(i)
            continue
        
        if len(stack) == 1: 
            res += s[stack[0]+1 : i]
           
        stack.pop() 
    
    return res

s = "(()())(())(()(()))"  

print(removeOuterParentheses(s))