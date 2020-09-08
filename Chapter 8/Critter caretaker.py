# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:09:46 2020

@author: Andrew
"""


#Critter Caretaker
#A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __str__(self):
        rep = "Critter object\n"
        rep += "Name: " + self.name + "\n"
        rep += "Hunger: " + str(self.hunger) + "\n"
        rep += "Boredom: " + str(self.boredom)
        return rep
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "content"
        elif 10 <= unhappiness <= 15:
            m = "sad"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood,"now.\n")
        self.__pass_time()
             
    def eat(self, food):
        print("Brruppp. Thank you")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        
    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
#main()
def main():
    crit_name = input("What do you want to name your critter?")
    crit = Critter(crit_name)
    
    choice = None
    while choice != "0":
        print("""
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter""")
        
        choice = input("Choice: ")
        print()
        
        #exit
        if choice == "0":
            print("Goodbye")
            
        #talk
        elif choice == "1":
            crit.talk()
            
        #feed
        elif choice == "2":
            food_amount = int(input("How much would you like to feed it?: "))
            crit.eat(food_amount)
            
        #play
        elif choice == "3":
            play_amount = int(input("How much would you like to play?: "))
            crit.play(play_amount)
            
        #secret display
        elif choice == "4":
            print(crit)
            
        else:
            print("Sorry, but", choice, "isn't a valid choice")
            
main()

input()