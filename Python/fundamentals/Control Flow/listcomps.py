mycomp = [v for v in range(5, 25)]
print(mycomp)

nums = range(25)
test = [lastone := v for v in nums]  # := is a walrus operator, the variable is assigned a value and returned at the same time
print(lastone)

board = [['_'] * 3 for i in range(3)]
print(board)
