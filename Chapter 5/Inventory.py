#thank god we're on to lists

INVENTORY = ["sword", "cake", "gold", "gems"]
i = 0

print(INVENTORY)

INVENTORY[0] = "crossbow"

for item in INVENTORY:
    if item == "cake":
        del INVENTORY[i]
        print("biug")
    i += 1



print(INVENTORY)

