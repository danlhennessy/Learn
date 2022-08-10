from time import perf_counter

t1 = perf_counter()
print("Hello World")
t2 = perf_counter()

print(f"Start , Stop: {t1} , {t2}")

print(f'Duration: {t2 - t1}')