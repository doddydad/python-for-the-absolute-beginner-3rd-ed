# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:35:14 2020

@author: Andrew
"""


# Mad Lib
# Create a story based on user input

from tkinter import *

class Application(Frame):
    """A GUI application to contain mad libs"""
    def __init__(self, master):
        """Initialise Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Create widgets to take input and display story. """
        #Create instruction label
        Label(self,
              text = "Enter information to create a story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # Create a label end text entry for the name of the person
        Label(self,
              text = "Person: "
              ).grid(row =1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
        
        # Create a label and text entry for a plural noun
        Label(self,
              text = "Enter a plural noun: "
              ).grid(row = 2, column = 0, sticky = W)
        self.plural_ent = Entry(self)
        self.plural_ent.grid(row = 2, column = 1, sticky = W)
        
        #Create a label and text entry for a verb
        Label(self,
              text = "Verb: "
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        
        # Create a label for adjective check buttons
        Label(self,
              text = "Adjective(s): "
              ).grid(row = 4, column = 0 , sticky = W)
        
        #The adjective check buttons
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "itchy",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)
        
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "joyous",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)
        
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "electric",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)
        
        self.is_beautiful = BooleanVar()
        Checkbutton(self,
                    text = "beautiful",
                    variable = self.is_beautiful
                    ).grid(row = 4, column = 4, sticky = W)
        
        # Create a label for body parts radio button
        Label(self,
              text = "Body Part: "
              ).grid(row = 5, column = 0, sticky = W)
        
        # Body part radio buttons
        self.body_part = StringVar()
        self.body_part.set(None)
        
        body_parts = ["bellybutton", "big toe", "hippocampus"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
            
        # Create a submit button
            
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        
        self.story_txt = Text(self, width = 75, height =10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)
        
    def tell_story(self):
        """ Fills the textbox with story from user input"""
        # Get the values
        person = self.person_ent.get()
        noun = self.plural_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_joyous.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "
        if self.is_beautiful.get():
            adjectives += "beautiful, "
            
        body_part = self.body_part.get()
        
        #create the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life long search for the lost city of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + "."
        story += " A strong, "
        story += adjectives
        story += "perculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + "."
        story += " And then, the "
        story +=  noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
        
        # Display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

#Main    
root = Tk()
root.title("Mad Libs")
app = Application(root)
root.mainloop()