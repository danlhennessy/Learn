#Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Dan", "age": 29, "city": "New York"}
print(mydict)

element = mydict["name"]
print(element)

#Add/Del Key-Value pair
mydict["somenum"] = 2 + 1
mydict["somenum"] += 23
del mydict["name"]
print(mydict)

#Check Key is in dict
if "name" in mydict:
    pass

for key, value in mydict.items():
    print(key, value)
    
print(mydict.values())

mydict2 = {"name": "Dan", 1: 3}
print(mydict2)
print(mydict2[1])
print(mydict2["name"])