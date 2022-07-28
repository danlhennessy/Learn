numbers = [1,2,3,4,5,6,74,8,9]

#Assign index as a variable to each item in list, then take action as below, one by one.
for index in numbers:
    if index >= 5:
        print(index + 100)
    else:
        print(index - 100)
        
#List Comprehension
numbers3 = [1,2,3,4,5,6,7,8,9,16]
newnumbers3 = []

for i in numbers3:
    newnumbers3.append(i+30)
print(newnumbers3)

onelinenumbers3 = [v - 2 for v in numbers3]
print(onelinenumbers3)

rangelist = [1,4,6,77,81,93]

#Print indexes of the list (0,1,2,3 etc)
for i in range(len(rangelist)):
    print(i)

#Print items in the list (1,4,6,77,81,93)    
for i in rangelist:
    print(i)
