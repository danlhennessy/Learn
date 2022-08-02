list1 = [1,2,3,4,5,6,7]

#Print first item in list
print(list1[0])

list1[0] += 3
print(list1[0])

grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
]
#print item in 1st row, 1st column
print(grid[0][0])

#Print item in 2nd row, 3rd column
print(grid[1][2])


emptylist = list()
print(emptylist)

#Lists allow different data types together
list3 = [5, True, "Apple"]

#Print last item in list
print(list3[-1])

#Confirm item exists in list
if "Apple" in list3:
        print("yes")
        
#List append + List insert
list3.append("Lemon")

list3.insert(2, "Orange")

print(list3)

#List pop + List remove
list3.pop()

list3.remove("Orange")

print(list3)

list4 = [1,4,3,7,8,5,]

#List sort and reverse
list4.sort()
list4.reverse()
sortedlist4 = sorted(list4)

print(list4)

#One Line list comprehension

def convert(list):
    return ([str(v) for v in list])

print(convert([1,2,3,4]))

#List comprehension to remove all instances of an element, in this case the highest number:
mylist1 = [1,2,3,4,5,6,6,6,6]
mylist2 = [v for v in mylist1 if v != max(mylist1)]
print(mylist2)