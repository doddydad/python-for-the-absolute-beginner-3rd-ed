#Word reverser
NEW_WORD = ""

WORD = input("type your word here:")
for letter in WORD:
    NEW_WORD = letter + NEW_WORD
print(NEW_WORD)
input()
