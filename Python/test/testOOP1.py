class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)
    
    def display(self):
        print(f"My name is {self.name} I am {self.age} years old")
        
class Student(Person):
    def __init__(self, name, age, section):
        self.section = section
        super().__init__(name, age)
        
    def displayStudent(self):
        print(self.name, self.age, self.section)
        
mystud = Student("Tony", 17, "Oak")

mystud.displayStudent()