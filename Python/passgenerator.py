import random
import string

def passgen():
    length = random.randint(10, 15)
    password = ''
    for c in range(length):
        password = password + random.choice(string.ascii_uppercase)
    print(password)


def passgen_withnumbers():
    length = random.randint(10, 15)
    password = ''
    for c in range(length):
        password = password + random.choice(string.ascii_uppercase + string.digits)
    print(password)

passgen()
passgen_withnumbers()