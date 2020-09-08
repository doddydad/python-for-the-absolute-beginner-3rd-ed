# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:30:24 2020

@author: Andrew
"""

# Asteriods Crash 07
# Adds music and scorekeeping


# Bugs:
# Only one sound effect at a time
#   big idk
# Can't fire at 45 degrees and missile and ship overlap with square sprites
#    Maybe now "fixed" by extending buffer
# New issue arising from said fix. Asteroids kill you before you overlap at all

# Todo add varying ammounts of health to things

import math, random
from livewires import games, color


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
    HEALTH = 1

    def update(self):
        """ Check for overlapping sprites """

        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.HEALTH -= 1
            self.HEALTH -= 1

        if self.HEALTH <= 0:
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

    POINTS = 30

    total = 0

    def __init__(self, game, x, y, size):
        """ Initialise asteroid sprite """
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size
        self.HEALTH = size
        self.game = game

        Asteroid.total += 1

    def update(self):
        """ Reduced health """
        super(Asteroid, self).update()

        if self.HEALTH <= 0:
            self.die()

    # Confused why course wants me to make this.
    def die(self):
        """ Destroy the asteroid and make more """
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game,
                                        x=self.x,
                                        y=self.y,
                                        size=self.size-1)
                games.screen.add(new_asteroid)

        # Checks to see if need to advance a level
        if Asteroid.total == 0:
            self.game.advance()

        super(Asteroid, self).die()


class Ship(Collider):
    """ The Player's Ship """
    image = games.load_image("ship.png")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    MAX_VELOCITY = 3
    MISSILE_DELAY = 25
    sound = games.load_sound("thrust.wav")

    def __init__(self, game, x, y):
        """ Initialise the ship """
        super(Ship, self).__init__(image=Ship.image,
                                   x=x, y=y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        """ Rotate based on keys pressed """
        # Rotation control
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        # Velocity control
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi / 180  # radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        self.dx = min(max(self.dx, -Ship.MAX_VELOCITY), Ship.MAX_VELOCITY)
        self.dy = min(max(self.dy, -Ship.MAX_VELOCITY), Ship.MAX_VELOCITY)

        # Firing missiles is more complex
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        super(Ship, self).update()
        if self.missile_wait > 0:
            self.missile_wait -= 1

    def die(self):
        """ Destroys the ship and ends the game """
        super(Ship, self).die()
        self.game.end()


class Game(object):
    """ The game itself """

    def __init__(self):
        """ Initialise the game object """
        self.level = 0

        self.sound = games.load_sound("level.wav")

        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right=games.screen.width-10,
                                is_collideable=False)
        games.screen.add(self.score)

        self.ship = Ship(game=self,
                         x=games.screen.width/2,
                         y=games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """ PLaying the game """
        games.music.load("theme.mid")
        games.music.play(-1)

        nebula_image = games.load_image("nebula.jpg")
        games.screen.background = nebula_image

        self.advance()

        games.screen.mainloop()

    def advance(self):
        """ Advance to next level of the game """
        self.level += 1

        # Amount of space around ship when it's created
        BUFFER = 200

        # Asteroid creation
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            x %= games.screen.width
            y %= games.screen.height

            new_asteroid = Asteroid(game=self,
                                    x=x, y=y,
                                    size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

        # Display level number
        level_message = games.Message(value="Level"+str(self.level),
                                      size=40,
                                      color=color.yellow,
                                      x=games.screen.width/2,
                                      y=games.screen.height/10,
                                      lifetime=3*games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)

        # Play new level sound
        if self.level > 1:
            self.sound.play()

    def end(self):
        """ End the game """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()


main()
