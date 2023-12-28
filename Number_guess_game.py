import random

rand_number = random.randrange(1,50)
guesses = 0
while True:
    guesses +=1
    UserInput = str(input("Guess a number between 1 and 50 \n"))
    if UserInput.isdigit():
        UserInput = int(UserInput)
    else:
        print("Please enter a number")
        continue

    if UserInput == rand_number:
        print("Wow you got it right")
        break
    elif UserInput > rand_number:
        print("Oops you are above the number")
    else:
        print("Oops you are below the number!")
print(f"You got it in {guesses} guesses")