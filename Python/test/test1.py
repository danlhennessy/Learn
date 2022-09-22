
mygen = (v for v in range(25) if v % 2 == 0)

print(next(mygen))
print(next(mygen))
print(next(mygen))

for v in mygen:
    print(v)