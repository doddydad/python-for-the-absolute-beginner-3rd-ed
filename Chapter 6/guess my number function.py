import random

#setting variables


#definitions

def ask_number(question = "", low = -99999, high = 99999, step = 1):
    """asks a for a number"""
    response = None
    while response not in range(low, high, step):
        try:
            response = int(input(question))
        except ValueError:
            print("This isn't a whole number")
    return response

def main():
    guess = "\n"
    attempts = 0
    print("guess my number")
    lower_bound = ask_number("what would you like the lower bound to be?:")
    upper_bound = ask_number("what would you like the upper bound to be?:")
    #these shouldn't be ask_number as the default range is large so takes ages
    the_number = random.randint(lower_bound, upper_bound)

    while guess != the_number:
        guess = ask_number("Take a Guess: ", lower_bound, upper_bound)
        if the_number < guess:
            print("too high")
        elif guess < the_number:
            print("too low")
        attempts += 1
    print("you won, the right answer was", the_number, "and it only took you", attempts,"tries")
    input()


#program

main()

