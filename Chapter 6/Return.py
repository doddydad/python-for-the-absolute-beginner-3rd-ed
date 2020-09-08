#Thing

def display(message):
    print(message)

def give_me_five():
    """testing some garbage"""
    five = 5
    return five

def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# main

display("here's a message for you\n")

number = give_me_five()
print("here's what I got from give_me_five():", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input()
