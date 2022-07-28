def myfunc(*args):
    for v in args:
        print(v)

        
myfunc('tony', 'lazer', 'cab')


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(f'Key: {k} Value: {v}')


myfunc2(key1=24, key2=12, testkey='Hello')
