####A simple password manager program###
####define your functions to use###

def view():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            username, passwd = data.split("|")
            print(f"Username: {username}")
            print(f"Password: {passwd}")
def add():
    name = input("Account Name:")
    psswd = input("Password:")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + psswd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add or view) | press q to quit \n").lower()
    if mode == "q":
        print("Goodbye!")
        break

    if mode == "add":
        add()

    if mode == "view":
        view()