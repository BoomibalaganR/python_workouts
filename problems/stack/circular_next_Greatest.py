def next_greatest(nums, stack): 
  
    res = [-1 for i in range(len(nums))]
    for i in range(len(nums)-1,-1,-1):
        
        while( len(stack) != 0 and stack[len(stack)-1] <= nums[i]):
            stack.pop() 
          
        if len(stack) != 0:
           res[i] = stack[len(stack)-1]
        
        stack.append(nums[i])
    return res

nums =  [1,2,3,4,3]
stack = [i for i in reversed(nums)] 

print(next_greatest(nums, stack) )


