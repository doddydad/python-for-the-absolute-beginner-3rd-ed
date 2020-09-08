#Tuple shit
import random
inventory = ()
item = ("",)

if not inventory:
    print("you aren't carrying anything")

while item != ("done",):
    item = (input("what item should you add to your inventory?:"),)
    if item != ("done",):
        inventory += item
dropped = random.randint(1, len(inventory))-1
print("oh no you dropped your", inventory[dropped],"how will you cope?")
inventory = inventory[0:dropped]+inventory[dropped+1: len(inventory)]
print("your inventory contains", len(inventory), "items, which are", inventory)
