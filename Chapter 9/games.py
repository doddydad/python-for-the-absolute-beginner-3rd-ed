# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:50:06 2020

@author: Andrew
"""


#Games
#Demos Module creation

class Player(object):
    """ A Player in a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
    
def ask_yes_no(question):
    """asks a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question = "", low = 0, high = 10, step = 1):
    """asks for a number"""
    response = None
    while response not in range(low,high,step):
        try:
            response = int(input(question))
        except ValueError:
            print("This isn't a whole number")
    return response

if __name__ == "__main__":
    print("You ran this module directly and didn't import is >:(")
    input()