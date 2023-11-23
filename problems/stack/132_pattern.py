
def find132_pattern(nums):
   
    size = len(nums) 
    for i in range(size):
       for j in range(i+1, size):
           for k in range(j+1, size):
               
               if nums[i] < nums[k] < nums[j]:
                   return True     
    return False

nums = [3,1,4,2] 
print(find132_pattern(nums))