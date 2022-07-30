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

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

comb_result = itertools.combinations(letters, 2)  # Provides all combinations of the provided iterable (Order does NOT matter)
print(list(comb_result))
perm_results = itertools.permutations(letters, 2) # Provides all permutations of the provided iterable (Order DOES matter)
print(list(perm_results))
result_with_repeats = itertools.combinations_with_replacement(numbers, 3) # Allow repeat characters
print(list(result_with_repeats))

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


