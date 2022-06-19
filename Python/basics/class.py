#Defines what a 'student' is (Something in your program that has a 'name, major, gpa, and is_on_probation' value
class student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
