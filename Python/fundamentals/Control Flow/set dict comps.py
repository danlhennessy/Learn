mylist = [1,3,3,4,5,7,7,8]
myset= {unique for unique in mylist if unique < 5}  # setcomp

employees = [("dan", 29), ("Fred", 22), ("Emma", 31)]
mydict = {name: age for name, age in employees}  # dictcomp
