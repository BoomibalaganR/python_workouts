from entity.student import Student  
from view import home_ui

from model.Api import Request

# this helper function do get name from student
def  get_name_from_student() -> str:
    while(True):   
            name = input("\nEnter your Name: ")   
            if name == "exit":
                return None
            if not name.isalpha(): 
                print("invalid literals..")  
                continue 
            return name
            
# this helper function do get grade from student 
def get_grade_from_student() -> list:
    
    grade_list = list()
    print("Enter your grade one by one if stop enter exit")  
    
    while(True):
        grade = input()  
            
        if grade == "exit":
            return grade_list 
        
        if grade.isnumeric():
            grade_list.append(int(grade)) 
        else: 
            print("enter valid grade...")




while(True):  

    home_ui.display()                                      # display the menu
    
    try:
        choice = int(input("Enter your choice: "))  
    except:
        print("enter valid literals")
        continue
 
    if choice == 1:                                         # add student
        while(True):
            name = get_name_from_student()                   # get student name
            
            if Request.is_studentExit(name) == "404":       # request for student name already exit or not
                break
            print("name already exits...!!") 
                
        
        if Request.create_student(Student(name)) == "200":   # request for create student
            print("successfully created....!!")

        input("\nplease enter to continue....")
        
    
    elif choice == 2:                                       # add grade 
        name =  get_name_from_student()                     # get name from student 
       
        if Request.is_studentExit(name) == "404":           # request for student name already exit or not
            print("name not found...!!")  
        else:  
            grade_list = get_grade_from_student()           # get grade from student
    
            if(len(grade_list) != 0 and
               Request.add_gradelist(name, grade_list) == "200"): # request for add gradelist to student
                print("successfully updated....!!")

        input("please enter to continue....")   
        
        
    elif choice == 3:                                      # get student average
        while(True):
            name = get_name_from_student()  
           
            if Request.is_studentExit(name) != "404":      # request for student name already exit or not
                break
            print("name not found..!!")             
 
        average = Request.get_student_average(name)           # request for get student average
        if average == "404":
            print("no grade available for calculate average") 
        else:
            print(average)
        
        input("please enter to continue....")       
    
    
    elif choice == 4:                                     # get class average
        class_average = Request.get_class_average()                # request for get class average
        print(class_average)
        input("please enter to continue....")       
    
        
    elif choice == 5:                                       # display grade
        while(True):
            name = get_name_from_student()                  # get name from student
           
            if Request.is_studentExit(name) != "404": # request for student name already exit or not
                break
            print("name not found..!!")     
            
        grade_list = Request.get_grade(name)        # request for get grade
        if grade_list == "404":
            print("no grades available..")
        else: 
            print(grade_list)                       # display all grade 
        input("please enter to continue....")
    
    
    elif choice == 6:                                   # exit 
        print("\n\t\t<<< Thank You >>>")      
        break 
    
    
    else:
        print("Enter valid choice...") 