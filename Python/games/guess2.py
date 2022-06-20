import random

x = 10
num = random.randint(1,x)
guess = 0

while guess != num:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < num:
        print("Too Low! Try again!")
    if guess > num:
        print("Too High, Try again!")
print(f"Nice Guess, the number was {num}")