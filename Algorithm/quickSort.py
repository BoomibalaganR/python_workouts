class Solution: 
 def qickSort(self, nums, left, right, key = lambda a: a ): 
    
    if left >= right: 
         return 
    i = left 
    j = right 
    pivot = nums[(left+right)//2] 
    
    while(i <= j): 
        while(key(nums[i]) < key(pivot)):  
            i += 1 
        while(key(nums[j]) > key(pivot)):  
            j -=1 
        
        if(i <= j): 
            nums[i], nums[j] = nums[j], nums[i]  
            i +=1 
            j -= 1
    
    self.qickSort(nums, left, i-1, key) 
    self.qickSort(nums, i, right, key)
    

 def frequencySort(self, s: str) -> str: 
        map = {} 
         
        for c in s: 
            if map.get(c) is None: 
                map[c] = 1 
            else: 
                map[c]+=1 
        ls = list(map.items())  

        print("before: ",ls)
        self.qickSort(ls, 0, len(ls)-1, key = lambda a: -a[1]);   
        print("after: ",ls)
        return "".join([item[0]*item[1] for item in ls])
        
       
       
       
obj = Solution() 
s = "2a554442f544asfasssffffasss"   
#s = "cccaaa"
ls = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]; 

obj.qickSort(ls, 0, len(ls)-1, key = lambda row: -row[2]) 
print(ls)
print(obj.frequencySort(s))