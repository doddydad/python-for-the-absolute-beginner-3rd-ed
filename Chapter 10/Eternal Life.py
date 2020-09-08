# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:53:20 2020

@author: Andrew
"""


# Longevity
# Demos text and entry widgets

from tkinter import *

class Application(Frame):
    """GUI to reveal secret to living a while"""
    def __init__(self, master):
        """Initialise the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Create button, text and entry widgets"""
        #create instruction label
        self.inst_lbl = Label(self, text = "Enter password to live forever")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # create label for password
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        
        # create an entry widget
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        
        # create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        
        #create a text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        
    def reveal(self):
        """Display message based on password"""
        contents = self.pw_ent.get()
        
        if contents == "secret":
            message = "Here's the secret to living for ever: " \
                "don't die."
        else:
            message = "Wrong password, so you must be a massive loser " \
                "and aren't worthy of the secret of eternal life"
                
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
        
# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()
        