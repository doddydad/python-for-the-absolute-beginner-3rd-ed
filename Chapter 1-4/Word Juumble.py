#Word Jumble
import random
WORDS = ("words","python","buttocks", "unreasonable", "chicken", "indian")
JUMBLE = ""
NEW_WORD = ()
GUESS = ""

print("""
Welcome to word jumble, you'll be shown a jumble and need to guess what
the word was originally""")      

#section to add to list
while NEW_WORD != ("no",):
    NEW_WORD = (input("""is there any additional word you would like available in the jumble?
if so type it here, if not type no:""").lower(),)
    if NEW_WORD != ("no",):
        WORDS += NEW_WORD

THE_WORD = WORDS[random.randint(0,len(WORDS))-1]
PRE_JUMBLE = THE_WORD

while PRE_JUMBLE != "":             #jumbles the specific word
    LETTER = random.randint(0,len(PRE_JUMBLE)-1)
    JUMBLE += PRE_JUMBLE[LETTER]
    PRE_JUMBLE = PRE_JUMBLE[:LETTER]+PRE_JUMBLE[LETTER+1:]

#[:x] is equivalent to [0:x}, and [x:] is equivalent to [x:the end of thing]


print(JUMBLE)

while GUESS != THE_WORD:
    GUESS = input("what do you think the word was originally?:").lower()
    if GUESS != THE_WORD:
        print("Sorry, try again")
    else:
        print("Correct, the answer was", THE_WORD)

input()
