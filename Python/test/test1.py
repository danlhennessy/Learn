

mylist = [1,5,'hello', 'take', True, (1, 4), 'fish']

print([v for v in mylist if type(v) is not str])