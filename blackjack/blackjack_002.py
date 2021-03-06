# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Blackjack" - Assignment 6
# 20141101

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
gamenum = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0],
                                                             pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cardlist = []

    def __str__(self):
        s = "Hand contains "
        t = ""
        for c in self.cardlist:
            t += str(c) + " "
        return s + t

    def add_card(self, card):
        # XXX: Note we are not creating Cards here.
        self.cardlist.append(card)

    def get_value(self):
        # XXX: Check
        """
        Count aces as 1; if hand has an ace add 10 if hand doesn't bust
        """
        value = 0
        for card in self.cardlist:
            value += VALUES[card.rank]
            if card.rank == "A" and value + 10 <= 21:
                value += 10
        print "Hand value", value
        return value

    def draw(self, canvas, pos):
        """
        Draw the back of the dealer's first card if the game is running, else every card's face, stack the cards.
        """
        counter = 0
        for card in self.cardlist:
            if in_play and counter == 0 and pos[1] == 140:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                                  [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                counter += 14.4
            else:
                card.draw(canvas, [pos[0] + counter, pos[1]])
                counter += 14.4


# define deck class
class Deck:
    def __init__(self):
        self.cardlist = [Card(s, r) for s in SUITS for r in RANKS]

    def shuffle(self):
        random.shuffle(self.cardlist)

    def deal_card(self):
        card = self.cardlist.pop()
        return card

    def __str__(self):
        s = "Deck contains "
        t = ""
        for c in self.cardlist:
            t += str(c) + " "
        return s + t


#define event handlers for buttons
def deal():
    # TODO: Remove debug printing
    global outcome, in_play, deck, player_hand, dealer_hand, gamenum
    gamenum += 1
    in_play = True
    deck = Deck()
    deck.shuffle()
    print deck
    player_hand = Hand()
    dealer_hand = Hand()
    print "Player " + str(player_hand)
    print "Dealer " + str(dealer_hand)
    print "Dealing  - Player"
    player_hand.add_card(deck.deal_card())
    print "Player " + str(player_hand)
    player_hand.add_card(deck.deal_card())
    print "Dealing  - Player"
    print "Player " + str(player_hand)
    print deck
    print "Dealing  - Dealer"
    dealer_hand.add_card(deck.deal_card())
    print "Dealer " + str(dealer_hand)
    dealer_hand.add_card(deck.deal_card())
    print "Dealing  - Dealer"
    print "Dealer " + str(dealer_hand)
    print deck


def hit():
    # TODO: Remove debug printing
    """
    If hand is in play, hit player. If busted, assign message to outcome, update in_play and score.
    """
    global in_play, outcome, score
    if in_play and len(deck.cardlist) > 0:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() <= 21:
            print str(player_hand)
            print "Player", player_hand.get_value()
            print outcome, score
        else:
            outcome = "You have busted."
            in_play = False
            score -= 1
            print str(player_hand)
            print "Player", player_hand.get_value()
            print outcome, score


def stand():
    # TODO: Remove debug printing
    """
    If hand is in play, repeatedly hit dealer until his hand has value 17 or more.
    Assign message to outcome, update in_play and score
    """
    global in_play, outcome, score
    if player_hand.get_value() > 21 and in_play:
        outcome = "You have busted."
        in_play = False
        score -= 1
        print "Player", player_hand.get_value()
        print outcome, score
    elif in_play:
        while dealer_hand.get_value() < 17 and len(deck.cardlist) > 0:
            dealer_hand.add_card(deck.deal_card())
            print "Dealer", str(dealer_hand)
            print "Dealer", dealer_hand.get_value()
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted."
            in_play = False
            score += 1
            print outcome, score
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = "Dealer won."
                in_play = False
                score -= 1
                print outcome, score
            else:
                outcome = "You won."
                in_play = False
                score += 1
                print outcome, score


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", [233.5, 40], 32, "Black", "sans-serif")
    canvas.draw_text("Game " + str(gamenum), [257.5, 80], 24, "Black", "sans-serif")
    canvas.draw_text("Score " + str(score), [247.5, 312], 24, "Black", "sans-serif")
    canvas.draw_text("Dealer", [40, 120], 24, "Black", "sans-serif")
    canvas.draw_text("You", [40, 440], 24, "Black", "sans-serif")
    dealer_hand.draw(canvas, [40, 140])
    player_hand.draw(canvas, [40, 464])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()