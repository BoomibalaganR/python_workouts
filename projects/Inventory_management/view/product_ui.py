from entity.product import Product 
from entity.discount_product import DiscountedProduct

def display(product):
    print("\n--------------------------------------------------------")
    print(" ID\t\tName\t\tPrice\t\tQuantity")  
    print("--------------------------------------------------------")
    
    if product == "400":
        print("\t\tno Record found..")
    else:  
        print(product)
    print("--------------------------------------------------------")
    