#Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Dan", "age": 29, "city": "New York"}
print(mydict)

element = mydict["name"]
print(element)

#Add/Del Key-Value pair
mydict["email"] = "fake@fake.com"
del mydict["name"]
print(mydict)

#Check Key is in dict
if "name" in mydict:
    pass

for key, value in mydict.items():
    print(key, value)
    
print(mydict.values())