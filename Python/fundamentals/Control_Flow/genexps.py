# Generator Expressions - Similar to listcomps but for building other sequence types - tuples, dicts etc
colours = ['red', 'blue', 'white']
sizes = ['small', 'medium', 'large']
symbols = '$¢£¥€¤'
mytup = tuple(ord(symbol) for symbol in symbols) # Creating a tuple from a generator expression
print(mytup)

for tshirt in (f'{c} {s}' for c in colours for s in sizes):  # Printing each tshirt as they are yielded using genexp
    print(tshirt)