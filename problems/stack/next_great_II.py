def nextGreatest_element(n):
    temp = n  
    rev = 0
    while temp != 0:
        digit = temp%10  
        rev = 10*rev + digit
        temp//=10 
    print(rev) 


n = 12 
nextGreatest_element(n)