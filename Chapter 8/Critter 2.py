# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:01:50 2020

@author: Andrew
"""


#Construtor Critter
#Demos construtors

class Critter(object):
    """A Virtual pet"""
    def __init__(self):
        print("A new critter has been born")
        
    def talk(self):
        print("\nHi I'm an instance of class critter")
        
#main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input()
