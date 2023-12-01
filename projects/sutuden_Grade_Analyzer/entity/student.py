
class Student: 
   
    def __init__(self, name): 
        self.__name = name.title() 
        self.__grade_list = []
        
    
    def get_name(self) -> str:
        return self.__name 
    
    def get_grade_list(self) -> list: 
        return self.__grade_list
    
    def set_grade(self, grade_list):
        for mrk in grade_list: 
            self.__grade_list.append(float(mrk))
        
    def to_dict(self):
        return dict(name = self.get_name(), grade_list = self.get_grade_list()) 