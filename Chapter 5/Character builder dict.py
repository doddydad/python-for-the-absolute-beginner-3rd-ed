#Character builder with dictionarys

#Starting Variables
i = 0
Change = ""
Stats = {"STRENGTH" : 0,
         "DEXTERITY" : 0,
         "CONSTITUTION" : 0,
         "WISDOM" : 0,
         "POOL" : 30}

print(
    "Your stats are: ",
    "\nStrength: ", Stats["STRENGTH"],
    "\nDexterity: " , Stats["DEXTERITY"],
    "\nConstitution: ", Stats["CONSTITUTION"],
    "\nWisdom: ", Stats["WISDOM"],
    "\nAnd you have", Stats["POOL"], "Points to still to spend",
    "\nType \"Exit\" to exit")


while i == 0:       #Dummy variable, never not true

    Stat = str(input("\nWhich stat would you like to change, full word please: ")).upper()
    if Stat in Stats:

        while Change == "":     #so it doesn't error if they type a non integer
            try:
                Change = int(input("""\nBy how much would you like to change it?
Negatives add it back to the pool: """))
            except ValueError:
                print("This is not a whole number")

        if Change + Stats[Stat] >= 0 and Change <= Stats["POOL"]:
            Stats[Stat] += Change
            Stats["POOL"] -= Change
            print("\nYour", Stat, "is now", Stats[Stat])
            print(
    "\nYour stats are: ",
    "\nStrength: ", Stats["STRENGTH"],
    "\nDexterity: " , Stats["DEXTERITY"],
    "\nConstitution: ", Stats["CONSTITUTION"],
    "\nWisdom: ", Stats["WISDOM"],
    "\nAnd you have", Stats["POOL"], "Points to still to spend",
    "\nType \"Exit\" to exit")

        elif Change + Stats[Stat] < 0:
            print("\nYour stats can't go below 0 silly, try again")

        elif Change > Stats["POOL"]:
            print("\nYou only have", Stats["POOL"],"points to spend sorry")

        Change = ""         #so the int checker works every time

    elif Stat == "EXIT":        #Obvious exit clause, loop never ends otherwise
        print(
    "Your stats are: ",
    "\nStrength: ", Stats["STRENGTH"],
    "\nDexterity: " , Stats["DEXTERITY"],
    "\nConstitution: ", Stats["CONSTITUTION"],
    "\nWisdom: ", Stats["WISDOM"],
    "\nGoodbye")
        break

    else:                   #Would love to accept contractions of keys, but don't know how
        print("\nThat's not one of the stats you can change, sorry, try again")

input()
