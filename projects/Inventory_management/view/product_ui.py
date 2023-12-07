
def display(response):
    print("\n--------------------------------------------------------")
    print(" Name\t\tPrice\t\tQuantity")  
    print("--------------------------------------------------------")
    
    if response["status_code"] == 404:
        print("\t\tno Record found..")
    else:  
      for product in response["data"]:
          print(product)
    print("--------------------------------------------------------")
    