#Main Concepts of Object-Oriented Programming (OOPs): Class, Object, Polymorphism, ncapsulatio, Inheritance, Data Abstraction

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
    
    def display(self):
        print(f"Max Speed is {self.max_speed}")
        print(f"Mileage is {self.mileage}")
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
        
class Bus(Vehicle):
    pass

bus2 = Bus("Tren", 160, 24)
print(bus2.seating_capacity(50))