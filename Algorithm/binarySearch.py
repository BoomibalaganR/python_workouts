def binarySearch(num, target): 
    
    low = 0 
    high = len(num)-1 
    
    while(low <= high): 
     
        mid = (low+high)//2  
     
        if(target == num[mid]):
            return mid 
        elif target < num[mid]:
            high = mid-1 
        else: 
            low = mid+1
    return -1  

# main  

nums = [1,2,3,4,5] 
print("Element present at: ",binarySearch(nums,4))