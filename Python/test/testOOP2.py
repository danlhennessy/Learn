class Car:
    def __init__(self) -> None:
        pass
    
mycar = Car

mycar.make = 'Ferrari'

print(mycar.make)

print(mycar.__dict__)
print(dir(mycar))