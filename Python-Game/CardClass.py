import random


##set up of all basic classes
class Card:
    def __init__(self, suits, values, suitnums):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Q", "K", "J"]
        self.suitnums = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

        ##set deck placeholder
        deck = []


        ##deck set up
        for suit in suits:
            for value in values:
                deck.append(Card(suit.values[suits], values, suitnums[values]))
        
                 
class PlayerHand:
    def __init__(self, cards):
        self.cards = cards

class Dealer:
    pass



        
        
 #self.suitnum = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
     
     
     
      # for str in self.nums:
        #     if self.value == "A":
        #         ## how to set for 1 or 11?