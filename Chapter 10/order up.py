# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:34:58 2020

@author: Andrew
"""


from tkinter import *

class Application(Frame):
    """A GUI for menu ordering"""
    
    def __init__(self, master):
        """initialising the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Creates all the widgets for the thing"""
        #welcome message
        Label(self,
              text = "Here's you menu I guess lol"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # Ask and receive table number
        Label(self,
              text = "Table Number: "
              ).grid(row = 1, column = 0, sticky = W)
        
        self.table_number = Entry(self)
        self.table_number.grid(row = 1, column = 1, sticky = W)
        
        # ordering starters
        Label(self,
              text = "What starter(s) would you like?"
              ).grid(row = 2, column = 0, columnspan = 2, sticky = W)
        
        # Choose starters
        self.snails = BooleanVar()
        Checkbutton(self,
                    text = "snails",
                    variable = self.snails
                    ).grid(row = 3, column = 0, sticky = W)
        
        self.soup = BooleanVar()
        Checkbutton(self,
                    text = "soup",
                    variable = self.soup
                    ).grid(row = 3, column = 1, sticky = W)
        
        self.shrimp_cocktail = BooleanVar()
        Checkbutton(self,
                    text = "shrimp cocktail",
                    variable = self.shrimp_cocktail
                    ).grid(row = 3, column = 2, columnspan = 2, sticky = W)
        
        # main meal, you can only have one
        Label(self,
              text = "What main would you like?: "
              ).grid(row = 4, column = 0, sticky = W)
        
        self.main_meal = StringVar()
        self.main_meal.set(None)
        
        main_meals = ["Lasagne", "Risotto", "Curry"]
        column = 0
        for meal in main_meals:
            Radiobutton(self,
                        text = meal,
                        variable = self.main_meal,
                        value = meal
                        ).grid(row= 5, column = column, sticky = W)
            column += 1
        
        # Button to change the text box response
        Button(self,
               text = "Order",
               command = self.order_meal
               ).grid(row = 6, column = 0, sticky = W)
        
        # Output text box
        self.meal_order_txt = Text(self, width = 50, height = 2, wrap = WORD)
        self.meal_order_txt.grid(row = 7, column = 0, columnspan = 4)
        
        
#    def order_meal(self):
#        self.table_number.grid_forget()
#    this hides a widget, but only one at a time. not viable menu system.        
        
    def order_meal(self):
        """Repeat the order back"""
        # Beginning of string
        meal_order = "Ok, we'll be back to you table "
        
        meal_order += self.table_number.get()
        
        meal_order += " soon with: "
        
        #Data from user
        if self.snails.get():
            meal_order += "snails, "
        if self.soup.get():
            meal_order += "soup, "
        if self.shrimp_cocktail.get():
            meal_order += "shrimp cocktail, "
        
        meal_order += "and your "
        meal_order += self.main_meal.get()
        
        # Display this
        self.meal_order_txt.delete(0.0, END)
        self.meal_order_txt.insert(0.0, meal_order)
        
#main
root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()