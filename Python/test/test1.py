

def fibbo():
    """Print all fibonacci numbers below 50
    """
    a, b = 0, 1
    while b + a < 50:
        a, b = b, a + b
        print(f'b = {b}')


if __name__ == '__main__':
    fibbo()