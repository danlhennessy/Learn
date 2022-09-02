one, two, *rest = [1,2,3,4,5,6,7,8,9,10]

print(two, rest)

some = {1: 'tree', 2: 'bush', 3: 'car', 4: 'road'}
others = {1: 'trees', 2: 'bushes', 3: 'cars', 5: 'roads'}

merged = {**some, **others}
print(merged)