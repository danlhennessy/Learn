# Cartesian product: Tuples

colours = ['red', 'blue', 'white']
sizes = ['small', 'medium', 'large']

products = [(c, s) for c in colours for s in sizes]

for p in products:
    print('colour: %s / size: %s' % p)  # %s formatting takes a tuple, in this case p and returns its values in order. Its is an example of tuple unpacking
# tuple unpacking:
city, year, pop = ('Tokyo', 2003, 32_450)

a, b, *rest = range(6)  # The * indicator, like with *args, is used in place of excess arguments/variables
print(a,b,rest)

print((*range(4), 4) == (0,1,2,3,4))  # The * can also be used on the right side of the definition, when creating iterables