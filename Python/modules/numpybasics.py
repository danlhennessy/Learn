import numpy as np

print(np.__version__)

a = np.array([1,22,31,4,5,6])
print(a)
b = np.append(a, 25)
c = np.insert(a, 3, 28) # Insert 28 at index 3
print(a, b, c)
if 25 in a:
    print("25 Appended to a")
if 25 in b:
    print("25 only Appended to copy of a")
if 28 in a:
    print("25 only Inserted to copy of a")

array6 = np.empty(6) # 6 Random digits, better than 6 0s for speed
print(np.arange(2, 9, 2))