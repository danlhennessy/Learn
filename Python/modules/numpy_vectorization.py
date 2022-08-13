import numpy as np

arr = np.arange(36).reshape(3,4,3)

a = np.array([1,22,31,4,5,6])
b = np.array([12,6,1,2,3,12])

print(a + 2)  # Mathmatical perations on np arrays will act on each element
print(a - b)  # The same applies when operating with other np arrays
print(a - np.minimum.accumulate(a))  #  For each int in a, print the diff between it and the cumulative minimum
print(np.max(a - np.minimum.accumulate(a)))  # Print the maximum difference from the above