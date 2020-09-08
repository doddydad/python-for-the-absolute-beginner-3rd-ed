# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:59:08 2020

@author: Andrew
"""


#Trivia thingy

#imports

import sys, pickle

#Definitions

#Grabs the file, exception built in
def open_file(file_name, mode):
    """opens file, exceptions built in"""
    try:
        the_file = open(file_name, mode)
    except IOError:
        print("Unable to open the file,", file_name,"closing the program")
        input()
        sys.exit()
    else:
        return the_file

#gets the next line. Demonstrates editing output
def next_line(the_file):
    """grabbs next line and formats"""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line
    
#Prints stuff
def welcome(title):
    """Just a print function basically"""
    print("Welcome to the quiz garbage I guess\n")
    print("\t\t", title,"\n")
    
#splits blocks from text file
def next_block(the_file):
    """grabs all the data from the next question"""
    category = next_line(the_file)
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)
    
    return category, question, answers, correct, explanation

#Using txt or dat, either is fine, don't inherit lists
#to use will ned to change which functions called
#not currently used
def show_highscores_txt():
    """shows highscores .txt"""
    try:
        highscores = open("highscores trivia.txt", "r")
        for line in highscores:
            print(highscores.readline())
            
        highscores.close()
    except IOError:
        highscores = open("highscores trivia.txt", "w")
        highscores.close()
        print("No highscores yet")  

#not currently used
def update_highscores_txt(score, name):
    """Updates and sorts highscores trivia.txt"""
    i = 0
    entry = str(score) + "\t\t" + name + "\n"
    
    #opens the file after making sure it exists
    highscores_file = None
    while highscores_file == None:
        try:
            highscores_file = open("highscores trivia.txt", "r")
        except ValueError:
            highscores_file = open("highscores trivia.txt", "w")
            highscores_file.close()

    #extracts from the file into a list
    highscores = highscores_file.readlines()
    highscores_file.close()

    #sorts the new score into the list
    while i <= len(highscores):
        if i == len(highscores):
            highscores.append(entry)
            break
        if int(entry[0:4]) > int(highscores[i][0:4]):
            highscores.insert(i, entry)
            break

        i += 1
    
    #writes new list to the file
    highscores_file = open("highscores trivia.txt","w")
    highscores_file.writelines(highscores)
    highscores_file.close()

def show_highscores_dat():
    """shows highscores .dat"""
    try:
        highscores_file = open("highscores trivia.dat", "rb")
        highscores = pickle.load(highscores_file)
        for item in highscores:
            print(item[0], "\t\t", item[1])
        highscores_file.close()
    except (IOError,EOFError):
        highscores = open("highscores trivia.dat", "wb")
        highscores.close()
        print("No highscores yet")

#Should check how you scored, and update the leaderboard
def update_highscores_dat(score, name):
    """adds new score and sort with .dat"""
    
    entry = (score, name)
    i = 0
    
    #extracts the list of highscores
    highscores_file = None
    while highscores_file == None:
        try:
            highscores_file = open("highscores trivia.dat", "rb")
            highscores = pickle.load(highscores_file)
            highscores_file.close()
        except EOFError:
            highscores_file = open("highscores trivia.dat", "wb")
            highscores = []
            pickle.dump(highscores, highscores_file)
            highscores_file.close()
    
    #sorts the new entry into the list of highscores
    while i <= len(highscores):
        if i == len(highscores):
            highscores.append(entry)
            break
        if int(entry[0]) > int(highscores[i][0]):
            highscores.insert(i, entry)
            break

        i += 1
    
    highscores_file.close()
    
    highscores_file = open("highscores trivia.dat", "wb")
    pickle.dump(highscores, highscores_file)
    highscores_file.close()

def main():
    """main"""
    
    #opening program
    trivia_file = open_file("trivia.txt", "r")
    title = trivia_file.readline()
    welcome(title)
    show_highscores_dat()
    name = input("What is your name?: ")
    score = 0

    
    #questions
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t",i+1, "-", answers[i])
        
        answer = input("What's your answer: ")
        
        question_score = int(next_line(trivia_file))
        if answer == correct:
            print("\nCorrect", end=" ")  
            score += question_score
        else:
            print("Sorry you're wrong and bad")
        print(explanation)
        print("Score",score,"\n\n")
        
        category, question, answers, correct, explanation = next_block(trivia_file)
        
    trivia_file.close()
    
    
    #update and show the highscores
    update_highscores_dat(score,name)
    show_highscores_dat()
    
    print("That was the last question, your score is", score)
    input()


main()
