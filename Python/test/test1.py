def mygen(num):
    n = 0
    while n < num:
        yield n
        n += 1
        
temp = mygen(20)
print(temp)
print(list(temp))

def mygen2(alist):
    i = 0
    for i in range(len(alist)):
        yield alist[i]
        i += 1
        
temp2 = mygen2([1,3,5,7,9,11,13,34])
print(list(temp2))