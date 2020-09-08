#hiscores

SCORES = []
CHOICE = None

while CHOICE != "0":
    print("""
High scores

0 - Exit
1 - Show Scores
2 - Add a Score
3 - Delete a Score
4 - Sort Scores
""")
    CHOICE  = input("Choice: ")

    #exiting program
    if CHOICE == "0":
        print("Good-Bye")

    #show scores
    elif CHOICE == "1":
        print("\nHigh Scores")
        for SCORE in SCORES:
            print(SCORE)

    #add a score
    elif CHOICE == "2":
        SCORE = int(input("what score did you get?: "))
        SCORES.append(SCORE)

    #remove a score
    elif CHOICE == "3":
        SCORE = int(input("Remove which score?: "))
        if SCORE in SCORES:
            SCORES.remove(SCORE)
        else:
            print(SCORE, "isn't in the highscore list")

    #sort scores
    elif CHOICE == "4":
        SCORES.sort(reverse=True)

    #catching garbage
    else:
        print("Sorry", CHOICE, "isn't a valid choice")

input()
            
        
        
