def generator():
    yield 1
    yield 2
    yield 3
    
for v in generator():
    print(v)