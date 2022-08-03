import numpy as np

a = np.array([1,22,31,4,5,6])
print(a)
b = np.append(a, 25)
c = np.insert(a, 3, 28) # Insert 28 at index 3
print(a, b, c)
if 25 in a:
    print("25 appended to copy of a")

arr = np.arange(36).reshape(3,4,3)  # 3 by 4 by 3 n-dimensional array
print(arr)