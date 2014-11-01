# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/#examples-hand_template.py
# http://www.codeskulptor.org/#examples-deck_template.py
# "Blackjack" - Assignment 6
# Class implementations
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
    # FIXME: This fucker never goes bust.
    # TODO: Remove debug printing
    """
    If hand is in play, hit player. If busted, assign message to outcome, update in_play and score.
    """
    global in_play, outcome, score
    p = player_hand.get_value()
    if in_play:
        if p <= 21:
            player_hand.add_card(deck.deal_card())
            print "Player", p
            if p > 21:
                outcome = "You have busted."
                in_play = False
                score -= 1
                # print "Player", p
                print outcome, score
    if p > 21:
        outcome = "You have busted."
        in_play = False
        score -= 1
        # print "Player", p
        print outcome, score


def stand():
    # TODO: Remove debug printing
    """
    If hand is in play, repeatedly hit dealer until his hand has value 17 or more.
    Assign message to outcome, update in_play and score
    """
    global in_play, outcome, score
    p = player_hand.get_value()
    d = dealer_hand.get_value()
    if p > 21:
        outcome = "You have busted."
        in_play = False
        score -= 1
        print "Player", p
        print outcome, score
    else:
        while d < 17:
            dealer_hand.add_card(deck.deal_card())
            print "Dealer", d
        if d > 21:
            outcome = "Dealer busted."
            in_play = False
            score += 1
            print outcome, score
        else:
            if p <= d:
                outcome = "Dealer won."
                in_play = False
                score -= 1
                print outcome, score
            else:
                outcome = "You won."
                in_play = False
                score += 1
                print outcome, score

deal()
print "-----------"
print "Testing"

#player_hand.add_card(deck.deal_card())
#print deck
#print "Player", player_hand.get_value()
#print "Dealer", dealer_hand.get_value()
#print "-----------"
#print "Hitting"
#hit()
#print "Player", str(player_hand)
#print "Player", player_hand.get_value()
#print outcome, score
#print "-----------"
#print "Standing"
#stand()
#print "Dealer", str(dealer_hand)
#print "Dealer", dealer_hand.get_value()
#th = Hand()
#th.add_card(Card("S", "A"))
#print "Test " + str(th)
#th.get_value()
#th.add_card(Card("C", "A"))
#print "Test " + str(th)
#th.get_value()
#th.add_card(Card("D", "A"))
#print "Test " + str(th)
#th.get_value()
#th.add_card(Card("H", "A"))
#print "Test " + str(th)
#th.get_value()

# c1 = Card("S", "A")
# c2 = Card("C", "2")
# c3 = Card("D", "T")
# print c1, c2, c3
# print type(c1), type(c2), type(c3)
#
#
# test_hand = Hand()
# print test_hand
#
# test_hand.add_card(c1)
# print test_hand
#
# test_hand.add_card(c2)
# print test_hand
#
# test_hand.add_card(c3)
# print test_hand
#
# print type(test_hand)

###################################################
# Output to console
# note that the string representation of a hand will
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains
#Hand contains SA
#Hand contains SA C2
#Hand contains SA C2 DT
#<class '__main__.Hand'>

###################################################
# Test code

# test_deck = Deck()
# print test_deck
# print type(test_deck)
#
# c1 = test_deck.deal_card()
# print c1
# print type(c1)
# print test_deck
#
# c2 = test_deck.deal_card()
# print c2
# print type(c2)
# print test_deck
#
# test_deck = Deck()
# print test_deck
# test_deck.shuffle()
# print test_deck
# print type(test_deck)
#
# c3 = test_deck.deal_card()
# print c3
# print type(c3)
# print test_deck

###################################################
# Output to console
# output of string method for decks depends on your implementation of __str__
# note the output of shuffling is randomized so the exact order of cards
# need not match

#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#<class '__main__.Deck'>
#DK
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ
#DQ
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5
#<class '__main__.Deck'>
#H5
#<class '__main__.Card'>
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3

###################################################
# Test code
## get_value
#c1 = Card("S", "A")
#c2 = Card("C", "2")
#c3 = Card("D", "T")
#c4 = Card("S", "K")
#c5 = Card("C", "7")
#c6 = Card("D", "A")
#
#test_hand = Hand()
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c2)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c5)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c3)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c4)
#print test_hand
#print test_hand.get_value()
#
#
#
#test_hand = Hand()
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c1)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c6)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c4)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c5)
#print test_hand
#print test_hand.get_value()
#
#test_hand.add_card(c3)
#print test_hand
#print test_hand.get_value()
#
#
#
###################################################
# Output to console
# note that the string representation of a hand may vary
# based on your implementation of the __str__ method

#Hand contains
#0
#Hand contains C2
#2
#Hand contains C2 C7
#9
#Hand contains C2 C7 DT
#19
#Hand contains C2 C7 DT SK
#29
#Hand contains
#0
#Hand contains SA
#11
#Hand contains SA DA
#12
#Hand contains SA DA SK
#12
#Hand contains SA DA SK C7
#19
#Hand contains SA DA SK C7 DT
#29