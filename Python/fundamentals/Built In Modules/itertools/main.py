import itertools # Itertools - Use cases: Combine, slice, flatten and group iterables

counter = itertools.count(start=5, step=-5)
print(next(counter))
print(next(counter))
print(next(counter))

data = [100, 200, 300, 400]
daily_data = list(itertools.zip_longest(range(10), data))  # Zip function by default stops when shortest iterable exhausts. This stops when longest exhausts
print(daily_data)

counter2 = itertools.cycle(['On', 'Off'])  # Cycles through iterable indefinitely
counter3 = itertools.repeat(2, times=3)  # Repeats item indefinitely or a number of times if set

squares = map(pow, range(10), itertools.repeat(2))  # Creaters an iterable with 0-9 ^2
print(list(squares))  # Iterables can be cast to a list to display values when printing