import random
the_number = random.randint(1,100)
guess = int(input("your guess:"))
tries = 0
while guess != the_number:
    if guess > the_number:
        print("too high")
    elif guess < the_number:
        print("too low")
    tries += 1
    guess = int(input("your guess:"))
print("correct, the answer was", the_number,"and that only took you", tries,"attempts")
