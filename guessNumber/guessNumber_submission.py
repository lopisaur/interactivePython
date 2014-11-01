__author__ = 'clopez'
# http://www.codeskulptor.org/#user38_xylYaBcC8C_6.py
# "Guess the number" - Assignment 2
# 20141004

#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from math import ceil, log
from random import randrange

tries = 0
the_number = 0
max_tries = 0
limit = 100

# Start and restart the game, if no value is passed, use 100.
def new_game():
    global tries, the_number, max_tries
    tries = 0
    the_number = randrange(1, limit + 1)
    # Game can be solved in log2(amount of numbers) guesses. Round it up and cast it as an integer.
    max_tries = int(ceil(log(limit, 2)))
    print "Guess a number between 1 and " + str(limit) + ". You have " + str(max_tries) + " chances."

# Event handlers to call the game with predefined ranges
def range100():
    global tries, limit
    tries = 0
    limit = 100
    new_game()


def range1000():
    global tries, limit
    tries = 0
    limit = 1000
    new_game()


def input_guess(guess):
    global tries
    tries += 1
    tries_left = max_tries - tries
    player_number = int(guess)
    if (player_number < 1 or player_number > limit) and tries_left > 0:
        print str(player_number) + " is not between 1 and " + str(limit) + "... Guesses left: " + str(tries_left)
    elif player_number == the_number:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
        new_game()
    elif player_number < the_number and tries_left > 0:
        print str(player_number) + " is too low. Guesses left: " + str(tries_left)
    elif player_number > the_number and tries_left > 0:
        print str(player_number) + " is too high. Guesses left: " + str(tries_left)
    elif tries_left <= 0:
        print str(player_number) + " is wrong too! You ran out of chances. Better luck next time.\n"
        new_game()


game_frame = simplegui.create_frame("Guess the number", 300, 300)
game_frame.add_button("New game (100)", range100, 150)
game_frame.add_button("New game (1000)", range1000, 150)
game_frame.add_input("Enter your guess", input_guess, 150)
game_frame.start()


new_game()
