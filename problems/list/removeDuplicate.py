
def remove_duplicate(lst):
    
    slow = 0 
    fast = 1
    
    while fast < len(lst):
        if lst[slow] != lst[fast]: 
            slow+=1
            lst[slow] = lst[fast] 
        fast+=1
    
    return slow


lst = [1,1,1,1,1] 
remove_duplicate(lst)
