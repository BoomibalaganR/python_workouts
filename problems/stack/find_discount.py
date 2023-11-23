
def final_price(price) -> list:
    
    stack = list()
    for i in range(len(price)-1, -1, -1):
        
      
        while len(stack) != 0 and stack[len(stack)-1] > price[i]:
            stack.pop() 
        if len(stack) == 0:
            print(price[i],"---> ",price[i]) 
        else:
            print(price[i],"--->",price[i] - stack[len(stack)-1]) 
        stack.append(price[i])


prices = [8,4,6,2,3]
final_price(prices)