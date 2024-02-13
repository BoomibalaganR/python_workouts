from model.Database.dbConnection import StudentDB
from model.entity.student import Student


# create student 
def create_student(student):
    if StudentDB.create(student.to_dict()):
        return "200" 


# add gradelist given name
def add_gradelist(name, grade_list): 
    updateStatus =  StudentDB.update({"name": name.title()}, {"grade_list": grade_list})  
   
    if updateStatus.modified_count != 0: 
        return "200"
   
   
# get student detail using name
def get_student_byName(name):
    student = StudentDB.read({"name": name.title()}) 
    if len(student) == 0:
        return "404" 
    return student[0] 

# check given student name exit or not
def is_studentExit(name):
    student = StudentDB.read({"name": name.title()}) 
    if len(student) == 0:
        return "404" 

# get grade list given name
def get_grade(name):
    student =  StudentDB.read_one({"$and": [{"name": name.title()}, {"grade_list": {"$ne": []}}]}, {"_id": 0, "grade_list": 1}) 
    if student is None:
        return "404" 
    return student


# get student average
def get_student_average(name): 
    
    pipeline = [    {"$match": {"name": name.title()}}, {"$unwind": {"path": "$grade_list"}}, 
                    {"$group": {"_id": "$name", "average": {"$avg": "$grade_list"}}}, 
                    {"$project": {"_id":0, "average": 1}}
                ]
    for document in StudentDB.aggregate(pipeline):
        return document
    return {"message": "no more grade to calculate average..."}


# get class average
def get_class_average():  

    pipeline = [
        {"$unwind": {"path": "$grade_list"}},
        {"$group": {"_id": "null", "class_average": {"$avg": {"$sum": "$grade_list"}}}}, 
    ]  
    for document in StudentDB.aggregate(pipeline): 
        return {"class_average": document["class_average"]} 
    
    return {"message": "no grade available for calculate average"}
    