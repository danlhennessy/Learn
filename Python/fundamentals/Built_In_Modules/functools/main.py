# functools - module for higher order functions (Functions that take other funcs as arguments OR return funcs as a result)
from functools import cache, lru_cache
import functools

def add(a: float, b: float):
    print(f'got args: {a=} {b=}')
    return a + b

add_6 = functools.partial(add, 6)  # Functools clean method for above make_adder function
print(add_6(12))

add_7 = functools.partial(add, b=7)  # Choose which arg to pass with arg=
print(add_7(12))

@lru_cache(maxsize=5)  # cache remembers previously computed numbers. Useful for avoiding slow repeated computations. lru_cache stores a set number of previous values
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(400):
        print(i, fib(i))
    print("finished")
    
if __name__ == '__main__':
    main()