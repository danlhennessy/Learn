#Return the maximum consecutive zeros in a string of binary e.g. "00000111010101100"

def consecutive_zeros(string):
    maxzeros = 0
    curzeros = 0
    for v in string:
        if v == "0":
            curzeros += 1
            if curzeros >= maxzeros:
                maxzeros = curzeros
        else:
            curzeros = 0

    return maxzeros

print(consecutive_zeros("01110000010101011"))