#Main Concepts of Object-Oriented Programming (OOPs): Class, Object, Polymorphism, Encapsulation, Inheritance, Data Abstraction

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
    
    def mileagesq(self):
        print(self.mileage ** 2)
        
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

bus2 = Bus("Tren", 160, 32)

print(bus2.name)

bus2.display()