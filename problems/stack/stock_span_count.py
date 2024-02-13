

def next(price: int, stack) -> int:
  
    for i in range(len(stack)-1, -1, -1): 
        
        while(len(stack) != 0 and stack[stack[len(stack)-1]] <= temperatures[i] ):
            stack.pop()

        if len(stack) != 0:
            res = stack[len(stack)-1] - i
            stack.append(i)  
        return res

prices =  [100, 80, 60, 70, 60, 75, 85] 
stack =list()

for price in prices:
    print(next(price, stack)) 
  