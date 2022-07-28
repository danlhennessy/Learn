#Unordered and mutable, like a list but does not allow duplicate entries

myset = {1,2,3,1,2}
print(myset)

#Convert a list into a set
mylist = [1,2,3,4,4,4,1,5,98]

myset2 = set(mylist)
print(myset2)

#Modify set
myset.remove(1)
myset.add(23)
print(myset)
