#! python3

import random

class Card:
    """Represents a standard playing card."""
    
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]    
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returning a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def deal_hands(self, num_hands, cards_per_hand):
        
        for hand_num in range(num_hands):
            hand_name = 'Hand number ' + str(hand_num+1)
            hand = Hand(hand_name)
            for card_num in range(cards_per_hand):
                hand.add_card(self.pop_card())
            print(f"{hand_name} has the following cards:")
            print(hand)

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

def main():
    new_deck = Deck()

    for i in range(50):
        new_deck.shuffle()

    new_deck.deal_hands(2, 5)

if __name__ == "__main__":
    main()