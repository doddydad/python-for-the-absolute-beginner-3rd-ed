# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:40:57 2020

@author: Andrew
"""


#Handle it
#mostly done this bit before

try:
    num = float(input("Enter a Number: "))
except ValueError:
    print("Use a number idiot")
    
#use exceptions when handling outside data (ie, getting form files or user)

#handle multiple exception clauses
print()

for value in (None, "Hi!", "5"):
    try:
        print("Attempting to convert", value,"-->",end=" ")
        print(float(value))
    except(TypeError):
        print("I can only convert a string or a number")
    except ValueError as e:
        print("Use a strong of digits")
        print(e)
    else:
        print("You entered the number")
        
