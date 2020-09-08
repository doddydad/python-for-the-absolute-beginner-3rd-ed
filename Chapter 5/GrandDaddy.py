#Who your daddy

Pairs = {"Andrew" : "Piers",
         "Peter" : "Piers",
         "Joe" : "Graham",
         "Graham" : "Peter"}


while 1 == 1:
    Menu = input(
"""
Type your selection
1 - Find someone's Daddy
2 - Find someone's GrandDaddy
3 - Add a pairing
4 - Edit a pairing
5 - Delete a pairing
6 - Print the table and exit
Type here: """)
    print("\n")

    if Menu == "1":
        Son = input("Who's dad do you want to look up?: ")
        if Son in Pairs:
            print("Their daddy is: ", Pairs[Son])

        else:
            print("We don't have any entry for them, you could add one in the menu")

    elif Menu == "2":
        Grandson = input("Who's Granddaddy do you want to look up?: ")
        if Grandson in Pairs:
            if Pairs[Grandson] in Pairs:
                print("Their Granddaddy is: ", Pairs[Pairs[Grandson]])

            else:
                print("They don't have a granddaddy in our table")

        else:
            print("They don't appear in our table at all")
        

    elif Menu == "3":
        Son = input("What's the name of the son?: ")
        Dad = input("What's the name of their dad?: ")
        Pairs[Son] = Dad

    elif Menu == "4":
        Son = input("Which son's pairing would you like to change?: ")
        if Son in Pairs:
            Dad = input("Who is their dad actually?: ")
            Pairs[Son] = Dad

        else:
            print("We don't have any entry for them, you could add one in the menu")

    elif Menu == "5":
        Son = input("Who's son's entry do you want to delete?: ")
        if Son in Pairs:
            del Pairs[Son]

        else:
            print("We don't have any entry for them, seems like someone was ahead of you")

    elif Menu == "6":
        print(Pairs)
        break

    else:
        print("Please enter one of the choices from the menu")
        
            
        
