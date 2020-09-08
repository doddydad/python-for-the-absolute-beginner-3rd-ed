#Guess the word game

#normal preliminary stuff
import random
WORDS = ("stuff", "words", "butts", "garbage", "relatable")
i = 0
#would be far better if could scrap a dictionary online for words

THE_WORD = WORDS[random.randint(0,len(WORDS)-1)]

print("you will get to guess whether 5 letters are in the word now")
while i < 5:
    LETTER = input("Guess a letter: ")
    if LETTER in THE_WORD:
        print("that letter is in the word")
    else:
        print("that letter is not in the word")
    i += 1

GUESS = input("what do you think the word is?: ").lower()
if GUESS == THE_WORD:
    print("Well done, the word was", THE_WORD)
else:
    print("Better luck next time!")

input()

