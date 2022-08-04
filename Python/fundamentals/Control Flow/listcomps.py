mycomp = [v for v in range(5, 25)]
print(mycomp)

nums = range(25)
test = [lastone := v for v in nums]  # := is a walrus operator, the variable is assigned a value and returned at the same time
print(lastone)

board = [['_'] * 3 for i in range(3)]
print(board)

mylist = [3,1,6,3,5,5,9,43,2,34,1]
print(id(mylist))
mylist = sorted(mylist)
print(mylist, id(mylist))