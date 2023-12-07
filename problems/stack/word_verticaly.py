
def printVertically(s): 
    ls = s.split(" ")
    i = 0   
    
    for s in ls:
        
        if i < len(s)-1: 
            print(s[i])


s = "HOW ARE YOU"  

printVertically(s)