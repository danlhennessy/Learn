import random

def guess():
    random_num = random.randint(1, 20)
    yourguess = 0
    while yourguess != random_num:
        yourguess = int(input('Guess a number between 1 and 20: '))
        if yourguess < random_num:
            print("Too Low!")
        elif yourguess > random_num:
            print("Too High")
    print(f"Well Done! The number was {random_num}")
    
guess()
