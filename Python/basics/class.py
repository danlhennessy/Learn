#Defines what a 'student' is (Something in your program that has a 'name, major, gpa, and is_on_probation' value
class student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
#Creating a 'student' object from the 'student' class       
student1 = student("Dan", "Azure", 3.1, False)
student2 = student("Pam", "Art", 3.4, True)

print(student1.name)

print(student2.gpa)