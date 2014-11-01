# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Blackjack" - Assignment 6
# 20141029

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

in_play = False
outcome = ""
score = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


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
        pass


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


def deal():
    # TODO: Remove debug printing
    global outcome, in_play, deck, player_hand, dealer_hand
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
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            print "Player", player_hand.get_value()
    if player_hand.get_value() > 21:
        outcome = "You have busted."
        in_play = False
        score -= 1
        print "Player", player_hand.get_value()


def stand():
    """
    If hand is in play, repeatedly hit dealer until his hand has value 17 or more.
    Assign message to outcome, update in_play and score
    """
    pass


def draw(canvas):
    # Blah
    card = Card("D", "2")
    card.draw(canvas, [300, 300])

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()