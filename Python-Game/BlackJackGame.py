
from subprocess import call
from colorama import Fore
import emoji
import time
import os
import random



#set to use clear 
def clear():
    call("clear" if os.name == "posix" else "cls")


##set up of Card class
class Card:
    def __init__(self, suit, card, card_value):
        self.suit = suit
        self.card = card
        self.card_value = card_value
    
    def __str__(self):
        return self.card + " of " + self.suit
        

##lists and dictionaries of card and card values
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Q", "K", "J"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

print(emoji.emojize("::"))

##deck set up
deck = []

## loop to establish 52 cards
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, cards_values[card]))


##function for game/game reference
def play_blackjack(self):

    global cards_values
    
    ##set holders for cards
    dealer_hands = []
    player_hands = []
   
    ##initial scores
    dealer_score = 0
    player_score = 0
    
    ##loop set up for game runs
    while len(player_hands) < 2:
        
    
        #card deal using random function
        player_card = random.choice(deck)
        player_hands.append(player_card)
        #takes card out of deck
        deck.remove(player_card)
    
        #score calculator
        player_score += player_card.card_value
    
        #Ace value swap 11 or 1 
        if len(player_hands) == 2:
            if player_hands[0].card_value == 11 and player_hands[1].card_value == 11:
                player_hands[0].card_value = 1
                player_score -= 10
    
        # Print player cards and score      
        print("PLAYER HAND: ")
        print(player_card)
        print("PLAYER SCORE = ", player_score)
    
        input(Fore.LIGHTCYAN_EX + "Press enter for next card\n" + Fore.RESET)
        
    
        #random card deal
        dealer_card = random.choice(deck)
        dealer_hands.append(dealer_card)
        deck.remove(dealer_card)
    
        #dealer score calculator
        dealer_score += dealer_card.card_value
    
        #print dealer card and score
        print("DEALER CARDS: ")
        print(dealer_card)
        if len(dealer_hands) == 1:
            print("DEALER SCORE = ", dealer_score)
        else:   
            print("DEALER SCORE = ", dealer_score - dealer_hands[-1].card_value)
    
    
        #set second card to different value to account for 11 or 1 for the Ace card
        if len(dealer_hands) == 2:
            if dealer_hands[0].card_value == 11 and dealer_hands[1].card_value == 11:
                dealer_hands[1].card_value = 1
                dealer_score -= 10
    
        input(Fore.LIGHTCYAN_EX + "Press enter...\n" + Fore.RESET)
    
        #different variations of scores and win/loss statements
        if player_score == 21:
            print(Fore.RED + (emoji.emojize(":money_bag:")) * 2 + "YOU HAVE BLACKJACK!!" + (emoji.emojize(":money_bag:")) * 2 + Fore.RESET)
            print(Fore.RED + (emoji.emojize(":confetti_ball: ")) * 2 + "YOU WIN!!" + (emoji.emojize(" :confetti_ball:")) * 2  + Fore.RESET)
            break
            play_blackjack(deck)

        elif dealer_score == 21:
            print(Fore.RED + "OH NO! \nDEALER HAS BLACKJACK!! YOU LOSE!" + (emoji.emojize(":money_with_wings:" + ":broken_heart:")) * 2 + "\n" + Fore.RESET)
            break
            play_blackjack(deck)

        while len(player_hands) == 2:
            if player_score > dealer_score and player_score < 21:
                print(Fore.RED + (emoji.emojize(":confetti_ball: ")) * 2 + "YOU WIN!!" + (emoji.emojize(" :confetti_ball:")) * 2 + Fore.RESET)
                break
                play_blackjack(deck)
            
            elif player_score > 21:
                print(Fore.RED + "BUST. YOU LOSE!!" + Fore.RESET)
                break
                play_blackjack(deck)

            elif dealer_score > player_score and dealer_score < 21:
                print(Fore.RED + (emoji.emojize(":thumbs_down:")) + "DEALER WINS!\nBETTER LUCK NEXT TIME" + (emoji.emojize(":thumbs_down:"))+ Fore.RESET + "\n")
                break
                play_blackjack(deck)
            
            elif dealer_score > 21:
                print(Fore.RED + "DEALER BUST\n YOU WIN!" + Fore.RESET)
                break
                play_blackjack(deck)

            else:
                player_score == dealer_score
                print(Fore.RED + (emoji.emojize(":red_circle: ")) + "PUSH" + (emoji.emojize(" :red_circle:")) + Fore.RESET)
                break
                play_blackjack(deck)
        

              
#method to call instructions in menu (very basic instructions)
def view_instructions(self):
    print(Fore.LIGHTCYAN_EX + "BASIC INSTRUCTIONS (not including splits, bets, doubling down, etc)" + Fore.RESET)
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

##menu
while True:
    #print centered welcome statement 
    greeting = Fore.RED + (emoji.emojize(":sparkles: ")) * 4 + "WELCOME TO THE BLACKJACK GAME!" + (emoji.emojize(" :sparkles:")) * 4 + "\n" + Fore.RESET 
    centered = greeting.center(78)

    print(Fore.LIGHTCYAN_EX + "\u2664    " * 4 + "\u2661    " * 4 + "\u2667    "* 4 + "\u2662    " * 4 + "\n")
    print(centered)
    print(Fore.LIGHTCYAN_EX + "\u2664    " * 4 + "\u2661    " * 4 + "\u2667    "* 4 + "\u2662    " * 4 + "\n" + Fore.RESET)
        
    #print choice option
    print("Choose an option from below and press enter: \n")  
    choice = int(input("""
        1. Start Game 
        2. View Instructions
        3. Reset
        4. Exit
        """))
    if choice == 1:
        play_blackjack(deck)    
    elif choice == 2:
        view_instructions(deck)
    elif choice == 3:
        clear()       
    else:
        #alignment and color setting for closing greeting
        greeting2 = Fore.RED + "THANKS FOR PLAYING! \n" + Fore.RESET
        centered2 = greeting2.center(78)

        #color and spacing setting for greeting
        print(Fore.LIGHTCYAN_EX + "\u2664    " * 4 + "\u2661    " * 4 + "\u2667    "* 4 + "\u2662    " * 4 + "\n" + Fore.RESET)
        print(centered2)
        print(Fore.LIGHTCYAN_EX  + "\u2664    " * 4 + "\u2661    " * 4 + "\u2667    "* 4 + "\u2662    " * 4 + "\n" + Fore.RESET)
        break
  
                    


                
        
        