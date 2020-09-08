# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#property critter
#demos properties

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("a new critter has been born")
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critters name can't be the empty string")
        else:
            self.__name = new_name
            print("Name change successful.")
            
    def talk(self):
        print("Hi I'm", self.name)
        
#main
crit = Critter("poochie")
crit.talk()

print("\nMy name is:", end = " ")
print(crit.name)

print("\nAttempting to change name of critter...")
crit.name = "Randolph"

print("\nMy critter's name is:", end = " ")
print(crit.name)

print("\nAttempting to change critters name ot empty string")
crit.name = ""

print("\nMy cirtters anem is:", end = " ")
print(crit.name)