# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:24:52 2020

@author: Andrew
"""

# Graphics not functional, game doesn't end.

from livewires import games, color

import random

games.init(screen_width=640, screen_height=480, fps=50)


class Paddle(games.Sprite):
    """ The Paddle the player controls """
    image = games.load_image("Paddle.png", transparent=False)

    def __init__(self):
        """ Create the paddle object """
        super(Paddle, self).__init__(image=Paddle.image,
                                     x=games.mouse.x,
                                     bottom=games.screen.height)

    def update(self):
        """ Updates paddle each frame """
        self.x = games.mouse.x

        if self.x < 0:
            self.x = 0
        if self.x > games.screen.width:
            self.x = games.screen.width

        self.check_collision()

    def check_collision(self):
        """ Checks if the ball has hit the paddle """
        # point of failure
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.dy = -sprite.dy


class Ball(games.Sprite):
    """ The ball bounding around """
    image = games.load_image("ball.jfif")
    # Nasty implementation, probably want to tie to score or bounces
    horizontal_speed = 1
    vertical_speed = 1

    def __init__(self):
        """ Creates the ball """
        super(Ball, self).__init__(image=Ball.image,
                                   x=random.randrange(640),
                                   y=100,
                                   dx=Ball.horizontal_speed,
                                   dy=Ball.vertical_speed)

    def update(self):
        """ Updates the balls movement """
        if self.x > games.screen.width:
            self.dx = -self.dx
        if self.x < 0:
            self.dx = -self.dx
        if self.y < 0:
            self.dy = -self.dy
        if self.dy > games.screen.height:
            self.die()

    def die(self):
        """ Ends the game """
        end_message = games.Message(value="Game over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=games.screen.fps*5,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    wall = games.load_image("Wall.jfif")
    games.screen.background = wall

    paddle = Paddle()
    games.screen.add(paddle)

    ball = Ball()
    games.screen.add(ball)

    games.screen.mainloop()


main()
