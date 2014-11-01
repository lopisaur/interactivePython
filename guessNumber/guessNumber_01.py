__author__ = 'clopez'
from math import ceil, log
from random import randrange

tries = 0
hundred = randrange(1, 101)
four_hundred = randrange(1, 401)
thousand = randrange(1, 1001)


def ghundred():
    global tries
    max_tries = int(ceil(log(100, 2)))
    if tries == 0:
        print "Guess a number between 1 and 100. You have " + str(max_tries) + " chances."
    elif tries == max_tries - 1:
        print "You guessed " + str(tries) + " times and have " + str(max_tries - tries) + " chance left."
    elif tries == 1:
        print "You guessed " + str(tries) + " time and have " + str(max_tries - 1) + " chances left."
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
#gthousand()

