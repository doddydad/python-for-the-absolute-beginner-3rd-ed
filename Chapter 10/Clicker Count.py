# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:48:33 2020

@author: Andrew
"""


# Click Counter
# Demos

from tkinter import *

class Application(Frame):
    """A GUI that counts button clicks"""
    def __init__(self, master):
        """Initialise the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
        
    def create_widget(self):
        """Create buttons that displays number of clicks"""
        self.bttn = Button(self)
        self.bttn["text"] = "Total Click: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
        
    def update_count(self):
        """ Increase click count and display new total """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
        
# Main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()