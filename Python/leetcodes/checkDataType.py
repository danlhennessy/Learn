#Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

def only_ints(val1, val2):
    if type(val1) is int and type(val2) is int:
        print(True)
    else:
        print(False)

only_ints("a", 4)
