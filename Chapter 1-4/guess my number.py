import random
attempts = 0
print("guess my number")
lower_bound = int(input("what would you like the lower bound to be?:"))
upper_bound = int(input("what would you like the upper bound to be?:"))
the_number = random.randint(lower_bound, upper_bound)
guess = False
while the_number != guess:
    guess = int(input("take a guess:"))
    if the_number < guess:
        print("too high")
    elif guess < the_number:
        print("too low")
    attempts += 1
print("you won, the right answer was", the_number, "and it only took you", attempts,"tries")
input()
