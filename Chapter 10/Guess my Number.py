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
              text="Welcome to guess my number!"
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # Getting name?
        Label(self,
              text="Name: "
              ).grid(row=1, column=0, sticky=W)

        self.name_ent = Entry(self)
        self.name_ent.grid(row=1, column=1, sticky=W)

        # Takes Upper and Lower bounds
        Label(self,
              text="Enter the upper and lower bounds the random number could be below"
              ).grid(row=2, column=0, columnspan=4, sticky=W)

        Label(self,
              text="Lower Bound: "
              ).grid(row=3, column=0, sticky=W)

        self.lower_bound_ent = Entry(self)
        self.lower_bound_ent.grid(row=3, column=1, sticky=W)

        Label(self,
              text="Upper Bound: "
              ).grid(row=3, column=3, sticky=W)

        self.upper_bound_ent = Entry(self)
        self.upper_bound_ent.grid(row=3, column=4, sticky=W)

        # Button to move to next page
        Button(self,
               text="Submit",
               command=self.choose_number
               ).grid(row=4, column=0, sticky=W)

        # The extra parts of the game
        Label(self,
              text="You now need to guess the number!"
              ).grid(row=5, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Your guess here: "
              ).grid(row=6, column=0, sticky=W)

        self.player_guess = Entry(self)
        self.player_guess.grid(row=6, column=1, sticky=W)

        # Button to check player guess against the number
        Button(self,
               text="Guess",
               command=self.check_guess
               ).grid(row=7, column=0, sticky=W)

        self.feedback_txt = Text(self, width=75, height=2, wrap=WORD)
        self.feedback_txt.grid(row=8, column=0, columnspan=5, sticky=W)

    def choose_number(self):
        """choose the random number based on the user's inputs"""

        # Informs the user if they entered useless info.
        try:
            lower_bound = int(self.lower_bound_ent.get())
            upper_bound = int(self.upper_bound_ent.get())
        except ValueError:
            message = "Please enter two integers as the bounds before you press submit"
            self.feedback_txt.delete(0.0, END)
            self.feedback_txt.insert(0.0, message)

        # the actual random selection
        self.the_number = random.randint(lower_bound, upper_bound)
        the_number = self.the_number

        # set the number of attempts at the number here
        self.attempts = 0

        # print a confirmation that they have created a number
        message = "You have now created a random number"
        self.feedback_txt.delete(0.0, END)
        self.feedback_txt.insert(0.0, message)

    def check_guess(self):
        """Checks the player's guess and then tells them the outcome"""
        # set variables
        the_number = self.the_number
        if self.player_guess.get() != "":
            guess = int(self.player_guess.get())
        attempts = self.attempts
        message = ""
        name = self.name_ent.get()

        # checking the guess and adjusting the message to be displayed

        message += name
        if the_number < guess:
            message += ", you guessed too high"
            attempts += 1
            message += " and it's taken " + str(attempts) + " attempts so far."
        elif guess < the_number:
            message += ", you guessed too low"
            attempts += 1
            message += " and it's taken " + str(attempts) + " attempts so far."
        elif guess == the_number:
            attempts += 1
            message += ", you were right! the answer was " + str(the_number) + "!\n" \
                "It only took you " + str(attempts) + " attempts."

        # update attempts and print
        self.attempts = attempts
        self.feedback_txt.delete(0.0, END)
        self.feedback_txt.insert(0.0, message)

# Main


root = Tk()
root.title("Guess my number")
app = Application(root)
root.mainloop()
