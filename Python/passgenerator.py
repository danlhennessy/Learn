import random
import string

def password_gen():
    length = random.randint(10, 15)
    for letter in password:
        letter = random.choices(string.ascii_uppercase + string.digits)
    print(password)
password_gen()