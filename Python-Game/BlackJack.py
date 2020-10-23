from CardClass import Card, PlayerHand, Dealer

deck = []

for suit in self.suits:
    for value in self.values:
        deck.append(Card(suit.values[self.suits], self.cards, self.suitnums[self.cards]))