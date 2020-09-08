# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:33:59 2020

@author: Andrew
"""


# Lazy Buttons
# Demos making buttons

from tkinter import *

# create a root window
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x200")

#Create a frame to hold widgets
app = Frame(root)
app.grid()

#Buttons
bttn1 = Button(app, text = "I o nothing")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me Too!")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same Here!"

# kick off loop
root.mainloop()