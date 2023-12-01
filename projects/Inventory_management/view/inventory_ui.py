from entity.product import Product

def display(productList):
    print("\n---------------------------------------------------------")
    print(" ID\t\tName\t\tPrice\t\tQuantity")  
    print("---------------------------------------------------------")
    
    if len(productList) == 0:
        print("\t\tno Record found..")
    else:  
        for product in productList: 
            print(product)
            #print(product["_id"],"\t\t",product["name"],"\t\t",product["price"],"\t\t",product["quantity"])
    print("---------------------------------------------------------")
