# Class vs Instance vs Local Variables


class shark():
    animaltype = "Fish"  # Class Variable, value shared by all objects of the class
    def __init__(self, name):
        self.name = name  # Instance Variable. Each object of class shark will have a unique value, depending on the parameter passed (name)
        
    def print_full_name(self):
        lastname = " Kai"  # Local Variable, only exists for the function it is within. Can't be called from outside. Useful as temp variables.
        print(self.name + lastname)

shark1 = shark("Bruce")
print(shark1.animaltype)  # Calling a Class Variable
print(shark.animaltype)  # Can also call Class variable directly from class
print(shark1.name)  # Calling an Instance Variable
shark1.print_full_name()