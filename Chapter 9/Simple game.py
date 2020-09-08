# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:57:57 2020

@author: Andrew
"""

#Simple Game
#Demos importing custom modules

import games, random


def main():
    print("Welcome to the world's simpliest game")
    
    again = None
    while again != "n":
        players = []
        num = games.ask_number(question = "How many players? (2 - 5): ", low = 2, high = 5)
    
        for i in range(num):
            name = input("Player name: ")
            
            score = random.randrange(100) + 1
            player = games.Player(name, score)
            players.append(player)
            
        print("\nHere are the game results")
        for player in players:
            print(player)
        
        again = games.ask_yes_no("Do you wanna play again (y/n): ")
    
    input()
    
main()