import random


##set up of all basic classes
class Card:
    def __init__(self, suits, values, suitnums):
        self.suits = suits
        self.values = values
        self.suitnums = suitnums

        
class PlayerHand:
    def __init__(self, cards):
        self.cards = cards

class Dealer:
    pass



##lists and dictionaries of card and card values
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Q", "K", "J"]
suitnums = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

##set deck placeholder
        deck = []


##deck set up
for suit in suits:
    for value in values:
        deck.append(Card(suit.values[suits], value, suitnums[values]))
        
                 


        
        
 #self.suitnum = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
     
     
     
      # for str in self.nums:
        #     if self.value == "A":
        #         ## how to set for 1 or 11?