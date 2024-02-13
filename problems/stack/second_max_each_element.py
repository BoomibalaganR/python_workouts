def next_greatest(nums): 
    stack = list() 
    res = [-1 for _ in range(len(nums))]
    
    
    for i in range(len(nums)-1, -1, -1):
     
        if 2 <len(stack):
            while len(stack) != 0 and stack[len(stack)-1] < nums[i]:  
                stack.pop()  
            
        if  2 <= len(stack)  :  
            res[i] = stack[len(stack)-2] 
            
        stack.append(nums[i])

        print("res",res) 
        print("stack",stack) 
        print()
    print(res)
    
nums = [2,4,0,9,6] 
next_greatest(nums) 