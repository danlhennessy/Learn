# Iterable is an object that you can iterate over. Iterators point to other iterables and can generate them with the __next__ method

myiterable = [1, 2, 3, 4, 5]
myiterator = iter(myiterable)

print(myiterator)
print(next(myiterator))
print(list(myiterator))  # Iterators are also always iterables, but iterables are not always iterators