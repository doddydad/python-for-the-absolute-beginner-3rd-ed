#better high scores

SCORES = []
CHOICE = None

#define a thing so that .sort() can sort by not first element
def sortsecond(val):
    return val[1]

while CHOICE != "0":
    print("""
High Scores better

0 - Quit
1 - List Scores
2 - Add a Score
""")

    CHOICE = input("Choice: ")
    print()

    #exit
    if CHOICE == "0":
        print("Cya nerd")

    #List scores
    elif CHOICE == "1":
        print("\n Highscores")
        print("NAME\tSCORE")
        for ENTRY in SCORES:
            SCORE, NAME = ENTRY
            print(NAME, "\t", SCORE)

    #edit scores
    elif CHOICE == "2":
        NAME = input("What's the players name?: ")
        SCORE = int(input("What did they score?: "))
        ENTRY = (NAME, SCORE)
        SCORES.append(ENTRY)
        SCORES.sort(key=sortsecond,reverse=True)
        SCORES = SCORES[:5]

    #garbage
    else:
        print("screw off with that garbage")

input()
