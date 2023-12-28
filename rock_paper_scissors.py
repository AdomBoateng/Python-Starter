import random

user_wins = 0
computer_wins = 0
options =["rock", "paper", "scissors"]

while True:
    UserInput = str(input("rock, paper or scissors  or Type q to quit \n").lower())
    if UserInput == "q":
        print("See you later")
        break

    if UserInput not in options:
        continue

    rand_number = random.randint(0,2)
    #rock = 0  paper=1  scissors=2
    computer_pick = options[rand_number]
    print(f"Computer picked {computer_pick}.")

    #Winning conditions
    if UserInput == "rock" and computer_pick == "scissors":
        print("Wow you won!")
        user_wins +=1
        continue

    elif UserInput =="paper" and computer_pick == "rock":
        print("Wow you won")
        user_wins += 1
        continue

    elif UserInput == " scissors" and computer_pick == "paper":
        print("Wow you won")
        user_wins += 1

    else:
        print("Oops you lost")
        computer_wins += 1
print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")

print("See you later")