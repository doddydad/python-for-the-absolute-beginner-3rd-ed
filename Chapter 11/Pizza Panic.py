# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:36:44 2020

@author: Andrew
"""

# Pizza Panic
# Player must must catch falling pzza before they hit the ground.

from livewires import games, color

import random

# Everything is tied to framerate FYI

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    """ Pan controlled by the player to catch falling pizza """
    image = games.load_image("trashcan.jpg")

    def __init__(self):
        """ Initialise pan object and text object for score """
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)

        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)

        games.screen.add(self.score)

    def update(self):
        """ Move to mouse x position """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Check if catch pizza """
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()

    def return_score(self):
        """ Returns score for other object's speed stuff """
        return self.score.value


class Pizza(games.Sprite):
    """ A pizza which falls to the ground """
    image = games.load_image("PIZZA.png")
    speed = 1

    def __init__(self, x, y=90):
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x, y=y,
                                    dy=Pizza.speed)

    def update(self):
        """ Check if pizza reached the bottom of the screen """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Destroy self if caught """
        self.destroy()

    def end_game(self):
        """ End the game """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """ A chef moving left and right and dropping pizzas"""
    image = games.load_image("chef.jpg")

    def __init__(self, y=55, odds_change=200):
        """ Initialise the chef object """
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=2)

        self.odds_change = odds_change
        self.time_til_drop = 0
        self.number_til_speed_increase = 0

    def update(self):
        """ Determine if direction needs to be reversed """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        """ Decrease countdown or drop pizza and reset cooldown """

        if self.time_til_drop > 0:
            self.time_til_drop -= 1

        else:
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)

            self.number_til_speed_increase += 1

            # set buffer to approx 30% of pizza height, regardless of pizza
            # speed. They drop more frequently as they move faster
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1

        if self.number_til_speed_increase >= 10:
            self.increase_speed()
            self.number_til_speed_increase -= 10

    def increase_speed(self):
        """ Increases the speed and therefore difficulty of everything """
        # Particularly the pizza speed might want to be changed more smoothly
        if self.dx > 0:
            self.dx += 1
        else:
            self.dx -= 1

        if self.dx % 2 == 0:
            Pizza.speed += 1

        if self.dx > 0:
            self.odds_change = int(400/self.dx)
        else:
            self.odds_change = int(400/-self.dx)


def main():
    """ Play the game """
    wall_image = games.load_image("wall.jfif", transparent=False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()


# Start it up!
main()
