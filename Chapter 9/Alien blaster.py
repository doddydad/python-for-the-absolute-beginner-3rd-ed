# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:15:43 2020

@author: Andrew
"""


#Alien Blaster
#Demos object interaction

class Player(object):
    """A player in a shooter game"""
    def blast(self, enemy):
        print("The Hero blasts an enemy")
        enemy.die()
        
class Alien(object):
    """An alien in a shooter game"""
    def die(self):
        print("I am kill")
        
#main
        
def main():
    print("Death of an enemy")
    
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    
    input()
    
main()
