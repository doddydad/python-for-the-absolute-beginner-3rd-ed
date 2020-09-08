# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:06:57 2020

@author: Andrew
"""


# Lazy Buttons 2
# Demos classes with tkinter

from tkinter import *

class Application(Frame):
    """A GUI Application with 3 buttons"""
    
    def __init__(self, master):
        """Initialise the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Creates three buttons"""
        # Create first button
        self.bttn1 = Button(self, text = "I do nothing!")
        self.bttn1.grid()
        
        #Create second button
        self.bttn2 = Button(self, text = "Me too")
        self.bttn2.grid()
        
        #Creates third button
        self.bttn3 = Button(self, text = "Me three")
        self.bttn3.grid()
        
#main
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)

root.mainloop()