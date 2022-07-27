# Decorators 

def decorator_func(original_func):
    def wrapper_func(*args):
        print(f'Wrapper executed this before {original_func.__name__}')
        return original_func(*args)
    return wrapper_func

@decorator_func  # Whenever display() is called, decorator_func also runs with display as the argument
def display():
    print('Display Function Ran')

@decorator_func    
def display_info(name, age):
    print(f'display info ran with args ({name},{age})')

display()
display_info('dan', 29)
