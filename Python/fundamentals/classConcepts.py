# Inheritance - Bringing functions from a base class to child classes

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def ageplusone(self):
        print(self.age + 1)


class gshep(dog):
    def __init__(self, name, age):
        super().__init__(name, age)  # Brings functions from base class including __init__
    
dog1 = gshep("joe", 28)

print(dog1.age)
dog1.ageplusone()

#Polymorphism - Base classes and child classes can contain the same functions. By default the child function will overwrite the base

class bird:
    def flight(self):
        print("Some birds can fly")
class penguin(bird):
    def flight(self):
        print("Penguins cant fly")
        
birdobj = bird()
penguinobj = penguin()
birdobj.flight()
penguinobj.flight()