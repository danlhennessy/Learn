#print(dir(int))

def convert(list):
    return ([str(v) for v in list])

print(convert([1,2,3,4]))

def addone(list2):
    return([v + 1 for v in list2])

print(addone([2,3,7,8]))