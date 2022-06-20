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