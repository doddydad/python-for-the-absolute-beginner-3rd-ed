#Hangman
import random

HANGMAN = (
"""
___________
|         |
|
|
|
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|
|
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|        -+-
|
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|       \-+-
|
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|       \-+-\\
|
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|       \-+-\\
|         |
|
|
|
|
|
|__________________
""",
"""
___________
|         |
|         0
|       \-+-\\
|         |
|         |
|        |
|        |
|
|
|__________________
""",
"""
___________
|         |
|         0
|       \-+-\\
|         |
|         |
|        | |
|        | |
|
|
|__________________
""")
MAX_WRONG = len(HANGMAN)-1
WORDS = ["PYTHON","VIDEOGAMES","OSTRACISED","TOFFEE","BREAK"]

#actual program from here

The_Word = WORDS[random.randint(0,len(WORDS)-1)].upper()
So_Far = "-" * len(The_Word)
Wrong  = 0
Used = []

while Wrong < MAX_WRONG and So_Far != The_Word:

    print(HANGMAN[Wrong])
    print("\n",So_Far)
    print("\nYou've already tried the following letters", Used,"\n")

    Guess = input("What letter would you like to guess?: ")[0].upper()
    while Guess in Used:
        print("You've already tried that one")
        Guess = input("Try a letter you've not used now: ").upper()
    Used.append(Guess)

    if Guess in The_Word:
        New = ""
        for i in range(len(The_Word)):
            if The_Word[i] == Guess:
                New += Guess
            else:
                New += So_Far[i]
        So_Far = New
        print("\n", So_Far)

    else:
        print("Sorry", Guess,"isn't in the word!")
        Wrong += 1

if Wrong == MAX_WRONG:
    print(Hangman[Wrong],"\n You've been hanged")

else:
    print("\n The word was", The_Word)

input()
    

    
            
    
