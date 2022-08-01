# functools - module for higher order functions (Functions that take other funcs as arguments OR return funcs as a result)
import functools

def add(a: float, b: float):
    print(f'got args: {a=} {b=}')
    return a + b

add_6 = functools.partial(add, 6)  # Functools clean method for above make_adder function
print(add_6(12))

add_7 = functools.partial(add, b=7)  # Choose which arg to pass with arg=
print(add_7(12))