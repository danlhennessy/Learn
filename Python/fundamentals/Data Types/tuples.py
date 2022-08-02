# Cartesian product: Tuples

colours = ['red', 'blue', 'white']
sizes = ['small', 'medium', 'large']

products = [(c, s) for c in colours for s in sizes]

for p in products:
    print('%s / %s' % p)