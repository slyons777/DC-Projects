import random

##set up of all basic classes
class Card:
    def __init__(self, suits, cards, suitnums):
        self.suits = suits
        self.cards = cards
        self.suitnums = suitnums

## use in menu later?
class Dealer:
    pass

##lists and dictionaries of card and card values
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Q", "K", "J"]
suitnums = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}


##set deck placeholder
deck = []


##deck set up
for suit in suits:
    for card in cards:
        deck.append(Card(suits[suit], card, suitnums[card]))

def play_blackjack(deck):

    global cards_values
    
    ##set holders for cards
    dealer_hands = []
    player_hands = []
   
    ##initial scores
    dealer_score = 0
    player_score = 0
    
    ##loop set up
    while len(player_hands) < 2:
    
        #card deal using random function
        player_card = random.choice(deck)
        player_hands.append(player_card)
        deck.remove(player_card)
    
        #score tally
        player_score += player_card.card_value
    
        #Ace value swap 11 or 1 
        if len(player_hands) == 2:
            if player_hands[0].card_value == 11 and player_hands[1].card_value == 11:
                player_hands[0].card_value = 1
                player_score -= 10
    
        # Print player cards and score      
        print("PLAYER HAND: ")
        print("PLAYER SCORE = ", player_score)
    
        input()
    
        # Randomly dealing a card
        dealer_card = random.choice(deck)
        dealer_hands.append(dealer_card)
        deck.remove(dealer_card)
    
        # Updating the dealer score
        dealer_score += dealer_card.card_value
    
        # Print dealer cards and score, keeping in mind to hide the second card and score
        print("DEALER CARDS: ")
        if len(dealer_hands) == 1:
            print("DEALER SCORE = ", dealer_score)
        else:   
            print("DEALER SCORE = ", dealer_score - dealer_hands[-1].card_value)
    
    
        #set second card to different value to account for 11 or 1 
        if len(dealer_hands) == 2:
            if dealer_hands[0].card_value == 11 and dealer_hands[1].card_value == 11:
                dealer_hands[1].card_value = 1
                dealer_score -= 10
    
        input()
    
        #player hits blackjack   
        if player_score == 21:
            print("YOU HAVE BLACKJACK!!")
            print("YOU WIN!!")
            quit()

def view_instructions(self):
    rules = """
    1. The goal of blackjack is to beat the dealer's hand without going over 21.
    Face cards are worth 10. 
    2. Aces are worth 1 or 11, whichever makes a better hand.
    3. Each player starts with two cards, one of the dealer's cards is hidden until the end.
    4. To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
    5. If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
    6. If you are dealt 21 from the start (Ace & 10), you got a blackjack.
    """
    print(rules)
                    


            
     
    