mystr = "Hello21mnfnfsd"
two_seven = slice(2, 7)
print(mystr[two_seven])

# Slicing to change mutable objects inplace:
mylist = list(range(12))
mylist[3:4] = 13, 19  # RHS must be an iterable
print(mylist)