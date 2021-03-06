# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:30:24 2020

@author: Andrew
"""

# Asteriods Crash 02
# Adds delay to missile fire rate

import math, random
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


def screenwrap(self):
    """ Wraps items through top and side of screen """
    if self.top > games.screen.height:
        self.bottom = 0
    if self.bottom < 0:
        self.top = games.screen.height
    if self.left > games.screen.width:
        self.right = 0
    if self.right < 0:
        self.left = games.screen.width


class Missile(games.Sprite):
    """ A missile what gets shot """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")

    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Initialise the ship missile """
        Missile.sound.play()
        angle = ship_angle * math.pi/180

        # Where missile starts
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # velocity
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # Create
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)

        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Move then destroy missile"""
        # Lifetime
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        # wrap
        screenwrap(self)


class Asteroid(games.Sprite):
    """ An asteroid which floats across the screen """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_med.bmp"),
              LARGE: games.load_image("asteroid_big.bmp")}

    SPEED = 2

    def __init__(self, x, y, size):
        """ Initialise asteroid sprite """
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size

    def update(self):
        """ Wrap around screen """
        screenwrap(self)


class Ship(games.Sprite):
    """ The Player's Ship """
    image = games.load_image("ship.png")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25
    sound = games.load_sound("thrust.wav")

    def __init__(self, x, y):
        """ Initialise the ship """
        super(Ship, self).__init__(image=Ship.image,
                                   x=x, y=y)
        self.missile_wait = 0

    def update(self):
        """ Rotate based on keys pressed """
        # Inputs
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi / 180  # radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # Firing missiles is more complex
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        # Standard upkeep and tracking
        screenwrap(self)
        if self.missile_wait > 0:
            self.missile_wait -= 1


# Creating the ship
the_ship = Ship(x=games.screen.width/2,
                y=games.screen.height/2)
games.screen.add(the_ship)


def main():
    # Establish background
    nebula_image = games.load_image("nebula.jpg", transparent=False)
    games.screen.background = nebula_image

    # Create 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.mainloop()


main()
