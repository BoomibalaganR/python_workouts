
def display(response):
    
    print("\n--------------------------------------------------------")
    print("\t\t\tSALES REPORT")  
    print("--------------------------------------------------------")
    if response["status_code"] == 204:
        print(response["message"]) 
        return 
    
    for report in response["data"]:
        print(report) 
    
    print("--------------------------------------------------------")