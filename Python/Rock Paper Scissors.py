import random
game = True
rps = ["Rock", "Paper", "Scissors"]
mychoice = random.choice(rps)


while game:
    mychoice = random.choice(rps)
    your_choice = input("Rock, Paper, Scissors?")
    print("Your " + your_choice + " Vs " + "My " + mychoice)
    if your_choice == "Rock" and mychoice == "Scissors":
        print("You Win!")
        game = False
    elif your_choice == "Scissors" and mychoice == "Paper":
        print("You Win!")
        game = False
    elif your_choice == "Paper" and mychoice == "Rock":
        print("You Win!")
        game = False
    elif your_choice == "Rock" and mychoice == "Paper":
        print("You lose! Try again...")
    elif your_choice == "Scissors" and mychoice == "Rock":
        print("You lose! Try again...")
    elif your_choice == "Paper" and mychoice == "Scissors":
        print("You lose! Try again...")
    else:
        print("It's a draw! Try again...")
