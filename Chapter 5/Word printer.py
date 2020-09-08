import random

WORDS = ["Hello", "Godbye", "Chicken", "Wings", "Icecream", "Banana"]

while len(WORDS) > 0:
    Selection = random.randint(0, len(WORDS)-1)
    print(WORDS[Selection])
    WORDS.remove(WORDS[Selection])
