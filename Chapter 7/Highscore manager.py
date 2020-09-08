# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:28:47 2020

@author: Andrew
"""


#Highscores

def score_collection():
    """Gets Score, Name"""
    
    score = None
    while score == None:
        try:
            score = str(input("What score did you get?: "))
        except ValueError:
            print("Integer please")
            
    name = input("What is your name?: ")
    
    return score, name

def highscore_manager(score, name):
    """For .txt format"""
    entry = score + "\t\t" + name + "\n"
    highscores_file = None
    while highscores_file == None:
        try:
            highscores_file = open("highscores.txt", "r")
        except ValueError:
            highscores_file = open("highscores.txt", "w")
            highscores_file.close()

    highscores = highscores_file.readlines()
    highscores_file.close()
    i = 0
    while i <= len(highscores):
        if i == len(highscores):
            highscores.append(entry)
            break
        if int(entry[0:4]) > int(highscores[i][0:4]):
            highscores.insert(i, entry)
            break

        i += 1
        

    highscores_file = open("highscores.txt","w")
    highscores_file.writelines(highscores)
    highscores_file.close()

def main():
    score, name = score_collection()
    while len(score) < 4:
        score = "0" + score
    
    highscore_manager(score, name)
        
main()
