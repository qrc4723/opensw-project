import random
from constants import *

SUITS = ['c', 's', 'h', 'd']
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
  
    def shuffle(self):
        random.shuffle(self.cards)
        

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
            
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 

    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != '1']
        aces = [c for c in first_card_index if c == '1']
        #print(aces)
        #print(non_aces)
        for card in non_aces:
            if card == '11' or card == '12' or card == '13':
                self.value += 10
            else:
                self.value += int(card)

        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1

    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)