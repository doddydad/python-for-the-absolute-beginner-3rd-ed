# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:57:44 2020

@author: Andrew
"""

# Sound and Music
# What do you think this demos

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

# load a sound file
missile_sound = games.load_sound("missile.wav")

# Load the music file
games.music.load("theme.mid")

choice = None
while choice != "0":

    print(
        """
Sound and Music

0 - Quit
1 - Play missile sound
2 - Loop missile sound
3 - Stop missile sound
4 - Play theme music
5 - Loop theme music
6 - Stop theme music
""")
    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Good-Bye.")

    # Play missile sound
    elif choice == "1":
        missile_sound.play()
        print("Playing missile sound")

    # Loop missile sound
    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        missile_sound.play(loop)
        print("Looping missile sound.")

    # Stop missile sound
    elif choice == "3":
        missile_sound.stop()
        print("Stopping missile sound")

    # Playing music
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")

    # Loop theme music
    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever(: "))
        games.music.play(loop)
        print("Looping theme music.")

    # Stop theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music")

    # Some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input()
