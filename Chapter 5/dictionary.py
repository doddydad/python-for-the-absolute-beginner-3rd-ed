# Dictionary stuff

# TODO, make all actions case insensitive

DICTIONARY = {
"osu!":"A rhythm game about clicking on circles",
"hollow knight":"metroidvania in greyscale",
"league of legends":"Major esport and moba with all the oversexualised women",
"warhammer2 tw":"strategy game about commanding and creating armies as 2 discrete actions"}

CHOICE = None

while CHOICE != "0":

    #set keys to be lower case meant to and doesn't
    #tuples in dictionary are immutable, they're tuples (immutable at least)
    #for loops only look at the key
    #for ENTRY in DICTIONARY:
    #    ENTRY = ENTRY.lower()
    #    print(ENTRY)
    #    print(DICTIONARY)

    print("""
Welcome to game dictionary

0 - Exit
1 - Search the Library
2 - Add an entry to the Library
3 - Modify an entry to the Library
4 - Delete an Entry
""")

    CHOICE = input("Choice: ")
    
    if CHOICE  == "0":
        print("cya nerd")

    elif CHOICE == "1":
        GAME = input("what game do you want to look up?: ").lower()
        print(GAME)
        print(DICTIONARY.get(GAME, "We don't have that one"))
        #if GAME in DICTIONARY.keys().lower():
        #    for ENTRY in DICTIONARY.keys():
        #        if ENTRY.lower() == GAME:
        #            print(DICTIONARY[ENTRY])
        #else:
        #    print("sorry about that")

    elif CHOICE == "2":
        GAME = input("What game you adding?: ").lower()
        if GAME not in DICTIONARY:
            DESCRIPTION = input("How would you describe it?: ")
            DICTIONARY[GAME] = DESCRIPTION
        else:
            print("that game is already in there")

    elif CHOICE == "3":
        GAME = input("what game's description would you like to change?: ").lower()
        if GAME in DICTIONARY:
            DESCRIPTION = input("How should this game be described?: ")
            DICTIONARY[GAME] = DESCRIPTION

    elif CHOICE == "4":
        GAME = input("What entry would you like to delete from the Library?: ").lower()
        if GAME in DICTIONARY:
            del DICTIONARY[GAME]
            print("yup", GAME, "Has been deleted")
        else:
            print("that game is already not there")

    else:
        print("that's not a valid choice")
        
input()
