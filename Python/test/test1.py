some_data = [1,2,3,"hello", (3, 5), True]

mygen = (value for index, value in enumerate(some_data) if index >= 1)

print(next(mygen))
print(next(mygen))