import random

def userChoice():
    user_choice = input("R for rock, S for scissors, P for paper: ")
    if user_choice == "R":
        return "rock"
    elif user_choice == "S":
        return "scissors"
    elif user_choice == "P":
        return "paper"
    else:
        print("Wrong input!")

options = ["rock", "scissors", "paper"]
computer_choice = random.choice(options)

def logic(userChoice, computerChoice):
    if userChoice == computerChoice:
        print("Draw!")
    elif userChoice == "scissors" and computer_choice == "paper" or userChoice == "paper" and computer_choice == "rock" or userChoice == "rock" and computer_choice == "scissors":
        print("Computer chosen: " , computerChoice)
        print("User wins!")
    else:
        print("Computer chosen: " , computerChoice)
        print("Computer wins!")

def main():
    while True:
        trigger = input("Do you want to continue?[Y/N]").upper()
        if trigger == "N":
            break
        elif trigger == "Y": 
            logic(userChoice(), computer_choice)
        else:
            print("Try again!")

main()