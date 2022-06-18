numbers = [1,2,3,4,5,6,7,8,9]

for index in numbers:
    if index >= 5:
        print(index + 100)
    else:
        print(index - 100)
        
    

#Modifying Original list (not recommended?)
numbers2 = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numbers2)):
    numbers2[i] += 2

print(numbers2)

#List Comprehension
numbers3 = [1,2,3,4,5,6,7,8,9,10]
newnumbers3 = []

for i in numbers3:
    newnumbers3.append(i+30)
print(newnumbers3)
