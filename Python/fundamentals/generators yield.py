#Generators are functions that return objects which can be iterated over. They are memory efficient for large data sets

def mygenerator():
    yield 1
    yield 2
    yield 3
    
for v in mygenerator():
    print(v)

g = mygenerator()
print(sum(mygenerator()))
value = next(g)
print(value) # Prints the next value in object g and pauses as that stage

value = next(g)
print(value)

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
    
cd = countdown(4)

next(cd) #When asking for next on a generator object, it will go through the function to the first yield line and stop at that point
print(next(cd)) #Prints the yielded num after 2 next runs, in this case will be 3

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

l = firstn(12) 
print(sum(firstn(12)))       
print(next(l))
print(next(l))
print(sum(l)) # Sum of rest of yield after first 2 nexts