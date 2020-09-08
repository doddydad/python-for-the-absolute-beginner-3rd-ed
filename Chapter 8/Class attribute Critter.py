# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:01:23 2020

@author: Andrew
"""


#Classy critters
#class attributes and static functions

class Critter(object):
    """a virtual pet"""
    total = 0
    
    @staticmethod
    def status():
        print("the total number of critters is", Critter.total)
        
    def __init__(self, name):
        print("A critter has been born")
        self.name = name
        Critter.total += 1
        
#main
print("Accessing the class attribute Critter.total:", end = " ")
print(Critter.total)

print("\n creating creatures")
crit1 = Critter("Lucy")
crit2 = Critter("Charlotte")
crit3 = Critter("Ben")

Critter.status()

print("\n Accessing the class attribute through an object:", end = " ")
print(crit1.total)

input()