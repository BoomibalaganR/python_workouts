from model.Database.db_operation import Database
from model.entity.product import Product 

from datetime import datetime



def add_product(product):
    if Database.create("products", product.to_dict()): 
       return {"status_code": 200, "message": "successfully added..."}                     # return success code
          

def get_all_product():
    return {"data": Database.read("products"), "status_code": 200 }                        # return list of product dictionary
    


def get_product_byID(product_id):                       # get product using id
    product = Database.read("products", {"_id": product_id})     # read from database
    if len(product) == 0:                               # if product is not found
        return "404"                                    # return not found code 
    
    return product[0]                                   # otherwise return product



def get_product_by_name(product_name, project):                  
    # get product_list from db
    product = Database.read("products", {"name": product_name}, project)  # read from database
   
    # check product_list is empty or not, if empty return
    if len(product) == 0:                               
        return {"status_code": 404, "message": "product not found..."}                                     
    
    return {"data": product, "status_code": 200, "message": "ok"}
    


def update_product(name, quantity):           # update product detail using id  
   
    # get product detail by name
    response = get_product_by_name(name, {"_id":0, "name":1, "quantity":1}) 
    
    # check if product exit or not
    if response["status_code"] == 404:
        return {"status_code": 404, "message": "product not found..."} 
    
    # get product_list from response
    product_list = response["data"]  
    
    # get actual quantity from product_list
    actual_quantity = product_list[0]["quantity"]  
    
    
    updated_quantity = actual_quantity + quantity 
    # check updatd quantity negative or not
    if updated_quantity <  0:
       return {"status_code": 304, "message": "quantity become negative..!"}  

    # update quantity
    updateStatus = Database.update("products", {"name": name}, {"quantity": updated_quantity })     # update product into DB
    
    # check if updated or not
    if updateStatus.modified_count == 1:                
        return {"status_code": 200, "message": "successfully updated...!"}  

   

def delete_product(product_name):                          
    delete_count = Database.delete("products", {"name":product_name})       
    
    if delete_count == 1:                 
        return {"status_code": 200, "message": "successfully deleted..."}    
    
    return {"status_code": 404, "message": "product not found..."}                                            


def add_customer(customer_name):
    
    query = {"customerName": customer_name.title()} 
    collection_name = "users" 
    
    customerID_list = Database.read(collection_name, query, project={})   
    if len(customerID_list) == 0: 
        return Database.create(collection_name, {"customer_name": customer_name})
 
    return customerID_list[0]["_id"]



def create_order(customer_name, product_name, ordered_quantity):
    
    # get product detail by name
    response = get_product_by_name(product_name, project={})  
    
    # check if product is exit if not , return
    if response["status_code"] == 404:
        return response
    
    # get product_list from response
    product_list = response["data"]   
    
    # get product_quantity from product_list
    available_quantity = product_list[0]["quantity"] 
    
    # check product stock if not return 
    if available_quantity == 0:
        return {"message": "Out Of Stock..!", "status_code": 0}
    
    # check ordered quantity less than the available quantity 
    if available_quantity < ordered_quantity:
        return {"message": "ordered quantity is more than the available quantity", 
                "status_code": 400}
  
    # get current date
    current_date = datetime.now()
    
    customer_id = add_customer(customer_name)
   
    # make dictionary of order_detail
    order_detail = {"customer_id": customer_id, "product_id": product_list[0]["_id"], 
                    "quantity": ordered_quantity, "date": current_date} 
 
   
    # create orders 
    if Database.create(collection_name="orders", data= order_detail):   
        
        # decrease the available quantity
        update_product(product_name, -1*ordered_quantity)
        return {"message": "successfully created order..", "status_code": 200}
   

     
def get_sales_report():

    pipeline = [
        {
            "$group": 
                {
                    "_id": "$product_id", "total_quantity":  {"$sum": "$quantity"}
                }
        }, 
          
	    {
            "$lookup": 
                {
                    "from": "products", "localField": "_id", "foreignField": "_id", "as": "product_detail" 
                } 
        }, 
     
        {
            "$unwind": 
                { 
                 "path": "$product_detail"
                }
        },
          
        {
            "$project": 
                {
                    "_id": 0, "product_name": "$product_detail.name", 
					"total_sales_amount": {"$multiply": ["$product_detail.price", "$total_quantity"]}
                }
        }
    ] 
     

    list_of_report = Database.aggregate("orders", pipeline) 
    
    if len(list_of_report) == 0:
        return {"status_code": 204, "message": "no sales Report available..."}

    return {"data": list_of_report, "status_code": 200 }
     
     
         
# get past purchase product ids by customer_id
def get_Allproduct_id_by_cutomerId(customer_id):
    pipeline =  [ 
                    {"$match": {"customer_id": customer_id}},
                    {"$group": {"_id": "$product_id"}},                  
                ] 
    
    list_of_dict_id = Database.aggregate(collection_name= "orders", pipeline= pipeline) 
    
    productId_list = [ document["_id"] for document in list_of_dict_id ]    
    return productId_list



# get similiar customer ids who are all purchase same product
def get_similiar_customer(recommended_customer_id, productId_list):

    pipeline =  [
                    {"$match":  
                        {"$and": [ {"customer_id":{"$ne" : recommended_customer_id }},
                        {"product_id":  {"$in": productId_list}}]}},  
                
                        {"$group": {"_id": "$customer_id"}}
               
                ]
    similiar_customer_ids = Database.aggregate(collection_name="orders", pipeline= pipeline)       
    
    return  [ document["_id"] for document in similiar_customer_ids]
    
    
        
def _get_recommend_product(similiar_customerId_list, num_recommendations):
          
        pipeline = [ 
                        {"$match": {"customer_id": {"$in": similiar_customerId_list}}},

                        {"$group": {"_id": {"customer_id": "$customer_id", "product_id": "$product_id"}, 
						            "total_quantity": {"$sum": "$quantity"}, 
                                    "purchase_count": {"$sum": 1}}}, 
	                    
                        {"$group": {"_id": "$_id.customer_id", 
						            "orders": {"$push": {"product_id": "$_id.product_id", 
                                    "purchase_count": "$purchase_count"}}}}, 


                        {"$unwind": {"path": "$orders"}},
                        {"$group": {"_id": "$orders.product_id", 
					            "purchase_count": {"$max": "$orders.purchase_count"}}},
  
	                    {"$sort": {"purchase_count": -1}},

                        {"$lookup": {"from": "products", "localField": "_id", "foreignField": "_id", "as": "product_detail"}},
                        
                        {"$limit": num_recommendations},
                        {"$project": {"_id": 0, "product_name": "$product_detail.name"}},
                ] 
               
               
        return Database.aggregate(collection_name= "orders", pipeline= pipeline)



def get_recommend_product(customer_name, num_recommendation):
    customer_list = Database.read(collection_name= "users", 
                                query= {"customer_name": customer_name.title()}, project= {}) 
    
    if len(customer_list) == 0:
        return {"status_code": 404, "message": "\ncustomer_name not found"} 
  
    customer_id = customer_list[0]["_id"]
   
    # get list of product who want to recommend 
    list_of_ids = get_Allproduct_id_by_cutomerId(customer_id)

    # get similiar customer_id 
    similiar_customer_list = get_similiar_customer(customer_id, list_of_ids)
   
    # get recommend product list
    recommended_product = _get_recommend_product(similiar_customer_list, num_recommendation)
   
   
    return {"data": recommended_product, "status_code": 200 }
    
    
    
def is_nameExit(name):
    response =  get_product_by_name(name, {"_id": 1})
    if response["status_code"] == 404:
        return {"status_code": 404, "message": "name not found"} 
    
    return {"status_code": 200 ,"message": "name already exits..."}

    
