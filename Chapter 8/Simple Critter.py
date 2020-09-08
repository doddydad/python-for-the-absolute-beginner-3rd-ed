# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:25:48 2020

@author: Andrew
"""


#Simple Critter
#demos basica class and object stuff

class Critter(object):
    """a virtual pet"""
    def talk(self):
        print("Hi, I'm an instance of class Critter")
        
#main
        
crit = Critter()
crit.talk()

input()