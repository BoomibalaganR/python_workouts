from model.Database.dbConnection import StudentDB
from entity.student import Student


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
    return student 


# get student average
def get_student_average(name): 
    student =  get_grade(name)  
    if student is None :
        return {"average": 0}
    
    grade_lists = student["grade_list"]
    
    tmark = 0
    for grade in grade_lists: 
       tmark+=grade 
    return {"average": tmark/len(grade_lists)}


# get class average
def get_class_average():
    class_gradeList = StudentDB.read({"grade_list": {"$ne": []}},{"_id": 0,"grade_list": 1}) 
    
    if len(class_gradeList) == 0:
        return {"class_average": 0} 
    
    class_total = 0
    for student in class_gradeList:
        for mark in student["grade_list"]: 
            class_total+=mark 
            
    return {"class_average": round(class_total/len(class_gradeList)-1, 2)} 