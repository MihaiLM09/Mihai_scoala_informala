import random
import os

if os.path.exists('cards.txt'):
    os.remove('cards.txt')

class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def show(self):
        with open('cards.txt', 'a', encoding='utf-8') as f:
            cardss = "{} {}".format(self.value, self.type)
            f.write(cardss)
            f.write('\n')
        print("{} {}".format(self.value, self.type))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.hand = []

    def build(self):
        for t in ['♠', '♣', '♦', '♥']:
            for v in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(t, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.hand.append(self.cards.pop())

    def showHand(self):
         for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()

for _ in range(10):
    deck.draw()

deck.showHand()

# ------------------------------------------------------------------------





