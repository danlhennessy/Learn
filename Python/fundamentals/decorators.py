def outer_func(message):
    
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('HI')
hi_func()