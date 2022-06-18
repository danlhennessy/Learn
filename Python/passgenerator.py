import random
import string

def password_gen():
    length = random.randint(10, 15)
    password = ''
    for letter in range(length):
        password = password + random.choice(string.ascii_uppercase)
    print(password)
password_gen()