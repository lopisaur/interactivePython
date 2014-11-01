__author__ = 'clopez'
# http://www.codeskulptor.org/#user38_IB0A77aDzv_8.py
from math import ceil, log
from random import randrange

tries = 0
the_number = 0
maxtries = 0
limit = 0


def newgame(passed=100):
    global tries
    global the_number
    global maxtries
    global limit
    limit = int(passed)
    the_number = randrange(1, limit + 1)
    maxtries = int(ceil(log(limit, 2)))
    maingame()


def hgame():
    global tries
    tries = 0
    newgame(100)


def tgame():
    global tries
    tries = 0
    newgame(1000)


def maingame():
    global tries
    if tries == 0:
        print "Guess a number between 1 and " + str(limit) + ". You have " + str(maxtries) + " chances."
    elif tries == maxtries - 1:
        print "You guessed " + str(tries) + " times and have 1 chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(maxtries - tries) + " chances left."
    else:
        print "You guessed " + str(tries) + " times and have " + str(maxtries - tries) + " chances left."
    player_number = int(input("Guess the number:\n"))
    tries += 1
    if player_number < 1 or player_number > limit:
        print "Between 1 and " + str(limit) + "... You have " + str(maxtries - tries) + " chances left."
        maingame()
    elif player_number == the_number and tries <= maxtries:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
    elif player_number < the_number and tries < maxtries:
        print str(player_number) + " is too low. Try again.\n"
        maingame()
    elif player_number > the_number and tries < maxtries:
        print str(player_number) + " is too high. Try again.\n"
        maingame()
    else:
        print str(player_number) + " is wrong too! You ran out of chances. Better luck next time.\n"

#hgame()
#tgame()
newgame()