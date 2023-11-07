def merge_two_list(list1, list2, m, n):
    
    i = m-1 
    j = n-1 
    k = m+n-1 
    
    while i >= 0 and j >=0:
        
        if list1[i] <= list2[j]:
            list1[k] = list2[j] 
            j-=1 
        else: 
            list1[k] = list1[i]
            i-=1 
        k-=1   
    while(j>=0):
        list1[k] = list2[j] 
        k-=1
        j-=1
   
# main 
list1 = [17,18,20,0,0,0] 
list2 = [1,2,3] 
m = 3
n = 3 

print("list1: ",list1) 
print("list2: ",list2)
merge_two_list(list1, list2, m, n)
print("\nmerge two list : ",list1)
