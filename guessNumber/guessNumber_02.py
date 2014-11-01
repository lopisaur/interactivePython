__author__ = 'clopez'

from math import ceil, log
from random import randrange

tries = 0
the_number = 0
max_tries = 0
limit = 0


def newgame(passed):
    global tries
    global the_number
    global max_tries
    global limit
    limit = int(passed)
    the_number = randrange(1, limit + 1)
    maxtries = int(ceil(log(limit, 2)))
    print "passed " + str(passed)
    print "limit " + str(limit)
    print "tries " + str(tries)
    print "the_number " + str(the_number)
    print "maxtries " + str(maxtries)
   # print "Guess a number between 1 and " + str(limit) + ". You have " + str(maxtries) + " chances."
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
    print "tries in main " + str(tries)
    print "the_number " + str(the_number)
    if tries == 0:
        print "Guess a number between 1 and " + str(limit) + ". You have " + str(max_tries) + " chances."
    elif tries == max_tries - 1:
        print "You guessed " + str(tries) + " times and have 1 chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(max_tries - tries) + " chances left."
    else:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chances left."
    player_number = int(input("Guess the number:\n"))
    tries += 1
    print "input " + str(player_number)
    if player_number < 1 or player_number > limit:
        print "I said between 1 and " + str(limit) + ". You have " + str(max_tries - tries) + " chances left."
        maingame()
    elif player_number == the_number and tries <= max_tries:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
    elif player_number < the_number and tries < max_tries:
        print str(player_number) + " is too low. Try again.\n"
        maingame()
    elif player_number > the_number and tries < max_tries:
        print str(player_number) + " is too high. Try again.\n"
        maingame()
    else:
        print str(player_number) + " is wrong too! You ran out of chances. Better luck next time.\n"

# hgame()
tgame()

"""

def ghundred():
    global tries
    max_tries = int(ceil(log(100, 2)))
    if tries == 0:
        print "Guess a number between 1 and 100. You have " + str(max_tries) + " chances."
    elif tries == max_tries - 1:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(max_tries - tries) + " chances left."
    else:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chances left."
    player_number = int(input("Guess the number:\n"))
    tries += 1
    if player_number == hundred and tries <= max_tries:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
    elif player_number < hundred and tries < max_tries:
        print str(player_number) + " is too low. Try again.\n"
        ghundred()
    elif player_number > hundred and tries < max_tries:
        print str(player_number) + " is too high. Try again.\n"
        ghundred()
    else:
        print str(player_number) + " is wrong too! You ran out of chances. Better luck next time.\n"


def gfourhundred():
    global tries
    max_tries = int(ceil(log(400, 2)))
    if tries == 0:
        print "Guess a number between 1 and 400. You have " + str(max_tries) + " chances."
    elif tries == max_tries - 1:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(max_tries - 1) + " chances left."
    else:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chances left."
    player_number = int(input("Guess the number:\n"))
    tries += 1
    if player_number == four_hundred and tries <= max_tries:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
    elif player_number < four_hundred and tries < max_tries:
        print str(player_number) + " is too low. Try again.\n"
        gfourhundred()
    elif player_number > four_hundred and tries < max_tries:
        print str(player_number) + " is too high. Try again.\n"
        gfourhundred()
    else:
        print "You ran out of chances. Better luck next time.\n"


def gthousand():
    global tries
    max_tries = int(ceil(log(1000, 2)))
    if tries == 0:
        print "Guess a number between 1 and 1000. You have " + str(max_tries) + " chances."
    elif tries == max_tries - 1:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(max_tries - 1) + " chances left."
    else:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chances left."
    player_number = int(input("Guess the number:\n"))
    tries += 1
    if player_number == thousand and tries <= max_tries:
        print str(player_number) + " is correct! You won after " + str(tries) + " guesses.\n"
    elif player_number < thousand and tries < max_tries:
        print str(player_number) + " is too low. Try again.\n"
        gthousand()
    elif player_number > thousand and tries < max_tries:
        print str(player_number) + " is too high. Try again.\n"
        gthousand()
    else:
        print "You ran out of chances. Better luck next time.\n"

ghundred()

#gfourhundred()
#gthousand()"""