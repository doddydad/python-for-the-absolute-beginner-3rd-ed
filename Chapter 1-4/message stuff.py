#message analyser
import random
message = input("you're a nobsack: ")
print("Your message is ", len(message),"characters long")
i = random.randint(1, len(message))
print("and contains the letter", message[i],"doesn't it")
print("The most common letter in the English language is 'e'", end = " ")
if "e" in message:
    print("and it's in your message")
else:
    print("but it's not in your message")
                   
