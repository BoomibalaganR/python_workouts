
def minRemoveToMakeValidParnthesis(s):
    
    stack = list()  
    removeList = list()
    
    for i in range(len(s)):
        
        if s[i] == "(":
            stack.append(i) 
        elif s[i] == ")" and len(stack) != 0 :
            stack.pop() 
        elif s[i] == ")" and len(stack) == 0:
            removeList.append(i) 
    
 
    res = str() 
    for i in range(len(s)):
        if i not in removeList and i not in stack: 
            res+=s[i] 
    return res
    

s = "))(("
print(minRemoveToMakeValidParnthesis(s))