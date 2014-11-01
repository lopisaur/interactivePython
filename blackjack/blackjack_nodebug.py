# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Blackjack" - Assignment 6
# Version without console debugging.
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
font = "sans-serif"
color = "Black"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


def halfmsgwidth(msg):
    return frame.get_canvas_textwidth(msg, 24, font) / 2


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
        for c in self.cardlist:
            s += str(c) + " "
        return s

    def add_card(self, card):
        self.cardlist.append(card)

    def get_value(self):
        """
        Count aces as 1; if hand has one ace add 10 if it would not bust.
        """
        value = 0
        aces = 0
        for card in self.cardlist:
            value += VALUES[card.rank]
            if card.rank == "A" and value + 10 <= 21 and aces == 0:
                value += 10
                aces += 1
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
        for c in self.cardlist:
            s += str(c) + " "
        return s


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, gamenum, score, xpos
    if not in_play:
        gamenum += 1
        outcome = "Hit or stand?"
        in_play = True
        xpos = 300 - halfmsgwidth(outcome)
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    else:
        outcome = "You lose."
        in_play = False
        score -= 1
        xpos = 300 - halfmsgwidth(outcome)


def hit():
    """
    If hand is in play, hit player. If busted, assign message to outcome, update in_play and score.
    """
    global in_play, outcome, score, xpos
    if in_play and len(deck.cardlist) > 0:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You have busted."
            in_play = False
            score -= 1
            xpos = 300 - halfmsgwidth(outcome)


def stand():
    """
    If hand is in play, repeatedly hit dealer until his hand has value 17 or more.
    Compare scores, assign message to outcome, update in_play and score
    """
    global in_play, outcome, score, xpos
    if player_hand.get_value() > 21 and in_play:
        outcome = "You have busted."
        in_play = False
        score -= 1
        xpos = 300 - halfmsgwidth(outcome)
    elif in_play:
        while dealer_hand.get_value() < 17 and len(deck.cardlist) > 0:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted."
            in_play = False
            score += 1
            xpos = 300 - halfmsgwidth(outcome)
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = "Dealer won."
                in_play = False
                score -= 1
                xpos = 300 - halfmsgwidth(outcome)
            else:
                outcome = "You won."
                in_play = False
                score += 1
                xpos = 300 - halfmsgwidth(outcome)


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", [233.5, 40], 32, color, font)
    canvas.draw_text("Game " + str(gamenum), [259, 80], 24, color, font)
    canvas.draw_text(outcome, [xpos, 270], 32, color, font)
    if not in_play:
        canvas.draw_text("New deal?", [244, 310], 32, color, font)
    canvas.draw_text("Score " + str(score), [259, 352], 24, color, font)
    canvas.draw_text("Dealer", [40, 120], 24, color, font)
    canvas.draw_text("You", [40, 440], 24, color, font)
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