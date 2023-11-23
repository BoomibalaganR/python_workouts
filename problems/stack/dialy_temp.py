def dailyTemperatures(temperatures): 
    
    size = len(temperatures)
    res = [0 for i in range(size)] 
    stack = list()  
    
    for i in range(len(temperatures)-1, -1, -1): 
        
        while(len(stack) != 0 and temperatures[stack[len(stack)-1]] <temperatures[i] ):
            stack.pop()

        if len(stack) != 0:
            res[i] = stack[len(stack)-1] - i
        stack.append(i)  
    return res
    


temperatures = [73,74,75,71,69,72,76,73]  
print(dailyTemperatures(temperatures))