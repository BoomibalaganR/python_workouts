

def form():
    while(True):
        product_name = input("Enter product Name: ")  # get product_name
        if product_name.isalpha(): 
            return product_name 
        print("enter valid literal....")
           

