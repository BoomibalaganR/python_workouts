from collections import deque

def re_arrange(lst):

    size = len(lst)
    sptr = 1
    lptr = size-1 
    q = deque()
    
    while sptr < size:  
        
        if sptr <= lptr:
            q.append(lst[sptr])
    
        if (sptr+1)%2 == 0:
         
            if sptr < lptr:
               lst[sptr] = lst[lptr] 
               lptr-=1  
            else:
                lst[sptr] = q.pop()
           
        else:  
            lst[sptr] = q.popleft()     
        sptr+=1  
     
  
# main 

lst = [i for i in range(1,10)] 
print("before: ",lst) 
re_arrange(lst) 
print("after:  ",lst)