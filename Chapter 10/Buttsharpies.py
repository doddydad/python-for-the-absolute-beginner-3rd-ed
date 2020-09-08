# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:20:42 2020

@author: Andrew
"""


#Labeler
#demos a label

from tkinter import *

# create the root window

root = Tk()
root.title("Buttsharpies")
root.geometry("200x50")

# create a frame to surround the the widgets

app = Frame(root)
app.grid()

# create a label in the frame
lbl = Label(app, text = "I'm a label")
lbl.grid()

#kick off the window's event loop
root.mainloop()
