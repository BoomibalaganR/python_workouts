def next_greatest(nums, dic): 
    stack = [] 
    for num in reversed(nums):
        
        while( len(stack) != 0 and stack[len(stack)-1] < num):
            stack.pop()
        if len(stack) != 0 and dic.get(num) is not None and num < stack[len(stack)-1]: 
            i = stack[len(stack)-1]
            dic[num] = i
        stack.append(num) 
    
    
a = [4, 1, 2]
nums = [1, 3, 4, 2]   

dic = { i:-1 for i in a}
next_greatest(nums, dic) 


