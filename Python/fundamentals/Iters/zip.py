nums = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b', 'c', 'd', 'e', 'f']

zipped = zip(nums, letters)  # zip creates an Iterator object, that combines multiple iterables into tuples containing the i'th value of each one

print(list(zipped))
# print(next(zipped))  # Once an iterator is 'used' it will return a StopIteration exception if you next it again

for n, l in zip(nums, letters):
    print(f'num: {n}')
    print(f'let: {l}')