
def decode_string(s):
    
    stack = list() 
    for char in s:
        if char == "]":
            temp = ""
            while(stack[len(stack)-1].isalpha()):
              temp=stack.pop()+temp 
            
            num = ""
            while(len(stack) != 0 and stack[len(stack)-1].isnumeric()): 
                num = stack.pop() + num 
            
            stack.append(int(num)* temp)
          
          
        if char.isalnum():
            stack.append(char)

    return "".join(stack)
    
    
s = "10[leetcode]"  

print(decode_string(s))
