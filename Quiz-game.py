#####A simple Quiz game using if-else statements###

print("Welcome to the Quiz game")

###################################
user_response = str(input("Do you want play a game? \n yes/no \n "))
if user_response.lower() == "yes":
    print("Okayy Let's play :)")
else:
    print("See you later then!")
    quit()

################Questions#####################
counter = 0
print("Question 1")
answer = str(input("What is the capital of France? \nA) London\nB) Paris\nC) Berlin\nD) Rome \n"))
if answer == "b":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")

print("Question 2")
answer = str(input("Which planet is known as the "'Red Planet'"?\nA) Venus\nB) Mars\nC) Jupiter\nD) Saturn \n"))
if answer == "c":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")
    counter = counter - 1

print("Question 3")
answer = str(input("What is the largest mammal in the world?\nA) Elephant\nB) Blue Whale\nC) Giraffe\nD) Polar Bear \n"))
if answer == "b":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")
    counter = counter - 1

print("Question 4")
answer = str(input("What is the powerhouse of the cell?\nA) Nucleus\nB) Mitochondria\nC) Ribosome\nD) Endoplasmic Reticulum \n"))
if answer == "b":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")
    counter = counter -1

print("Question 5")
answer = str(input("Which is the largest ocean on Earth?\nA) Atlantic Ocean\nB) Indian Ocean\nC) Southern Ocean\nD) Pacific Ocean \n"))
if answer == "d":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")
    counter = counter - 1
print("Question 6")
answer = str(input("Who is known as the 'Father of Computer Science'?""\nA) Alan Turing\nB) Bill Gates\nC) Steve Jobs\nD) Mark Zuckerberg \n"))
if answer == "a":
    print("Correct answer")
    counter = counter + 1
else:
    print("Incorrect answer")
    counter = counter - 1

#########################################
print(f"Your final mark is {counter}/6")