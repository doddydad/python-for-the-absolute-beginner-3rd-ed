# character builder

Pool = 30
Str = 0
Dex = 0
Wis = 0
Con = 0


while Pool > 0:
    Which = input("You have", Pool, " attributes still to spend \n do you want to ADD or REMove points").upper()
    if "REM" in Which:
        Stat = input("Which stat would you like decrease?: ").upper()
        if "STR" in Stat:
            Amount = input("How much would you like to change the stat by?: ")
            if Str >= Amount:
                Pool += Amount
                Str -= Amount
            else:
                print("
        
