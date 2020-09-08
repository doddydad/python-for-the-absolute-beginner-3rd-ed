#Word Jumble#

#sets the variables
import random
WORDS = (("words","clue 1"),
         ("python","clue 2"),
         ("buttocks","clue 3"),
         ("unreasonable","clue 4"),
         ("chicken","clue 5"),
         ("indian","clue 6"))
JUMBLE = ""
NEW_WORD = ""
GUESS = ""

#section to add to WORDS
#not yet working, NEW_ENTRY gets added as 2 strings despite being a tuple
#while NEW_WORD != "no":
#    NEW_WORD = input("""is there any additional word you would like available in the jumble?
#if so type it here, if not type no: """).lower()
#    if NEW_WORD != "no":
#        NEW_HINT = input("What should the hint be for this word?: ")
#        NEW_ENTRY = (NEW_WORD, NEW_HINT)
#        print(NEW_ENTRY)
#        WORDS = WORDS + NEW_ENTRY

print(WORDS)
#selects the word and its corresponding hint
#don't currently know how to call things multiple nests down in tuples
SELECTION = random.randint(0,len(WORDS))-1
THE_WORD = WORDS[SELECTION][0]
HINT = WORDS[SELECTION][1]
PRE_JUMBLE = THE_WORD

while PRE_JUMBLE != "":             #jumbles the specific word
    LETTER = random.randint(0,len(PRE_JUMBLE)-1)
    JUMBLE += PRE_JUMBLE[LETTER]
    PRE_JUMBLE = PRE_JUMBLE[:LETTER]+PRE_JUMBLE[LETTER+1:]

#[:x] is equivalent to [0:x}, and [x:] is equivalent to [x:the end of thing]


print(JUMBLE)
print("and your hint is:", HINT)

while GUESS != THE_WORD:
    GUESS = input("what do you think the word was originally?:").lower()
    if GUESS != THE_WORD:
        print("Sorry, try again")
    else:
        print("Correct, the answer was", THE_WORD)

input()
