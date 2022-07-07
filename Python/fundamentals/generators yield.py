#Generators are functions that return objects which can be iterated over. They are memory efficient for large data sets

def mygenerator():
    yield 1
    yield 2
    yield 3
    
for v in mygenerator():
    print(v)

g = mygenerator()

value = next(g)
print(value) # Prints the next value in object g and pauses as that stage

value = next(g)
print(value)