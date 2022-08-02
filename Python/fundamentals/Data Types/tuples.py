# Cartesian product: Tuples

colours = ['red', 'blue', 'white']
sizes = ['small', 'medium', 'large']

products = [(c, s) for c in colours for s in sizes]

print(products)