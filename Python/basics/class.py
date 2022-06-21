#Defines what a 'student' is (Something in your program that has 'name, major, gpa, and is_on_probation' parameters)
class student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False    
        
#Creating a 'student' object from the 'student' class       
student1 = student("Dan", "Azure", 3.1, False)
student2 = student("Pam", "Art", 3.7, True)

print(student1.name)

print(student2.gpa)

print(student2.on_honor_roll())