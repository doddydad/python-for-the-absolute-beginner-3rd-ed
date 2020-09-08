# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:30:24 2020

@author: Andrew
"""

# Asteriods Crash 07
# Adds explosions and removes redundant code


# Bugs:
# You can insta die if asteroids spawn on top of you.
# Only one sound effect at a time
# Can't fire at 45 degrees and missile and ship overlap with square sprites

import math, random
from livewires import games


# Everything is tied to framerate so change with caution
games.init(screen_width=640, screen_height=480, fps=50)


class Screenwrapper(games.Sprite):
    """ An object which wraps items through top and side of screen """

    def update(self):
        """ Wrap sprite around screen """
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self """
        self.destroy()


class Collider(Screenwrapper):
    """ Can also collide with objects """

    def update(self):
        """ Check for overlapping sprites """

        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy self and leave an explosion """
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Explosion(games.Animation):
    """ Explosion animation """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x, y=y,
                                        repeat_interval=4, n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


class Missile(Collider):
    """ A missile what gets shot """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")

    BUFFER = 50
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
        # Adminy stuff
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        super(Missile, self).update()


class Asteroid(Screenwrapper):
    """ An asteroid which floats across the screen """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_med.bmp"),
              LARGE: games.load_image("asteroid_big.bmp")}

    SPEED = 2
    SPAWN = 2

    def __init__(self, x, y, size):
        """ Initialise asteroid sprite """
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size

    # Confused why course wants me to make this.
    def die(self):
        """ Destroy the asteroid and make more """
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x=self.x,
                                        y=self.y,
                                        size=self.size-1)
                games.screen.add(new_asteroid)
        super(Asteroid, self).die()


class Ship(Collider):
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

        super(Ship, self).update()
        if self.missile_wait > 0:
            self.missile_wait -= 1


def main():
    # Establish background
    nebula_image = games.load_image("nebula.jpg", transparent=False)
    games.screen.background = nebula_image

    # Creating the ship
    the_ship = Ship(x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)

    # Create 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.mainloop()


main()
