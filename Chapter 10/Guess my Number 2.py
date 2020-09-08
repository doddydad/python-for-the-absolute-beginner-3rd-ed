# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:34:30 2020

@author: Andrew
"""


# Guess my number gui

from tkinter import *
import random

class Application(Frame):
    """A GUI for guess my number"""
    
    # Initialise the frame
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_starting_widgets()
        
    # Create the widgets on entry
    def create_starting_widgets(self):
        """Creates the widgets to accept player input to start the game"""
        # Greeting at the top
        Label(self,
              text = "Welcome to guess my number!"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # Getting name?
        Label(self,
              text = "Name: "
              ).grid(row = 1, column = 0, sticky = W)
        
        self.name_ent= Entry(self) 
        self.name_ent.grid(row = 1, column = 1, sticky = W)
        
        # Takes Upper and Lower bounds
        Label(self,
              text = "Enter the upper and lower bounds the random number could be below"
              ).grid(row = 2, column = 0, columnspan = 4, sticky = W)
        
        Label(self,
              text = "Lower Bound: "
              ).grid(row =3, column = 0, sticky = W)
        
        self.lower_bound_ent = Entry(self)
        self.lower_bound_ent.grid(row = 3, column = 1, sticky = W)
        
        Label(self,
              text = "Upper Bound: "
              ).grid(row = 3, column = 3, sticky = W)
        
        self.upper_bound_ent = Entry(self)
        self.upper_bound_ent.grid(row = 3, column = 4, sticky = W)
        
        # Button to move to next page
        Button(self,
               text = "Submit",
               command = self.choose_number
               ).grid(row = 4, column = 0, sticky = W)
        
        
    def choose_number(self):
        """choose the random number based on the user's inputs"""
        # Choose the random number, leave the first screen
        if self.lower_bound_ent.get() != "":
            lower_bound = int(self.lower_bound_ent.get())
        if self.upper_bound_ent.get() != "":
            upper_bound = int(self.upper_bound_ent.get())
        the_number = random.randint(lower_bound, upper_bound)
        
        self.guessscreen
        
    def guessscreen(self):
        """creates the second screen in which you guess the number"""
        Label(self,
              text = "You now need to guess the number!"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        Label(self,
              text = "Your guess here: "
              ).grid(row = 1, column = 0, sticky = W)
        
        self.player_guess = Entry(self)
        self.player_guess.grid(row = 1, column = 1, sticky = W)
        
        # Button to check player guess against the number
        Button(self,
               text = "Guess",
               command = self.check_guess
               ).grid(row = 4, column = 0, sticky = W)
        
    def check_guess(self):
        Label(self,
              text = ""
              ).grid(row = 0, column = 0, sticky = W)
        
    
        
# Main
        
root = Tk()
root.title("Guess my number")
app = Application(root)
root.mainloop()