# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:02:18 2020

@author: Andrew
"""

# Slippery Pizza
# Chasing thing with mouse game

from livewires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Pan(games.Sprite):
    """ A Pan controlled with the mouse"""
    def update(self):
        """ Move to mouse position. """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
        
    def check_collide(self):
        """ Check if collided with Pizza """
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
            
class Pizza(games.Sprite):
    """ A slippery pizza """
    def handle_collide(self):
        """ Move to a random screen location """
        self.x = random.randrange(0, games.screen.width)
        self.y = random.randrange(0, games.screen.height)
        
def main():
    wall_image = games.load_image("wall.jfif", transparent = False)
    games.screen.background = wall_image
    
    pizza_image = games.load_image("pizza.jfif")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    the_pizza = Pizza(image = pizza_image, x = pizza_x, y = pizza_y)
    games.screen.add(the_pizza)
    
    pan_image = games.load_image("trashcan.jpg")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)
    
    games.mouse.is_visible = False
    
    games.screen.event_grab = True
    
    games.screen.mainloop()
    

#Start

main()