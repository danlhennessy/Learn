from functools import wraps
import time
def decorator_func(original_func):
    @wraps(original_func)  # Used to copy over original function name/arguments etc rather than the wrapper func when used as a decorator
    def wrapper_func(*args):
        print(f'Wrapper executed this before {original_func.__name__}')
        return original_func(*args)
    return wrapper_func
class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func
    
    def __call__(self, *args):
        print(f'call method executed this before {self.original_func.__name__}')
        return self.original_func(*args)

def my_timer(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_func.__name__} ran in {t2}')
        return result
    return wrapper

@decorator_class # Can use the __call__ method of a class to achieve same result as using a decorator function
def display():
    print('Display Function Ran')

@decorator_func # Whenever display() is called, decorator_func also runs with display as the argument
@my_timer
def display_info(name, age):
    print(f'display info ran with args ({name},{age})')
    

display()
display_info('dan', 29)
