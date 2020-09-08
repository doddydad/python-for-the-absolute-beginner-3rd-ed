# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:34:14 2020

@author: Andrew
"""


#attribute critter
#demos attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born")
        self.name = name
        
    def __str__(self):
        rep = "Critter object/n"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Hi I'm", self.name, "\n")
        
#main
        
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Rudolph")
crit2.talk()

print("Printing crit1:", crit1)

print("Diretly accessing crit1.name:", crit1.name)

input()
