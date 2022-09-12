class Car:
    def __init__(self, age=5):
        self.test = 'hello'
        self.age = age
    
mycar = Car()

mycar.make = 'Ferrari'

print(mycar.make)

print(mycar.__dict__)
print(dir(mycar))

# print(mycar.age)
print(mycar.test)