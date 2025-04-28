"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck

class Hist(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments (or decrements) the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand."""

        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2:
                return True
        return False

    def has_two_pair(self):
        
        self.rank_hist()

        pair_counts = 0
        for count in self.ranks.values():
            if count == 2:
                pair_counts += 1
        if pair_counts == 2:
            return True
        return False

    def has_three_kind(self):
        
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    def has_four_kind(self):
        
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False

    def has_full_house(self):
        
        self.rank_hist()
        for val in self.ranks.values():
            if (val == 2) and (val==3):
                return True
        return False

    def has_straight(self): # everything works but this
        
        self.ranks = Hist()
        for c in self.cards:
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        #rank_set = { card['rank'] for card in self }

        #straight = ((max(rank_set) - min(rank_set) + 1) == len(self)) and (len(rank_set) ==  len(self))
        #return straight
        #self.rank_hist()
        #ranks = self.rank_hist
        #ranks[14] = ranks.get(1, 0)
        
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_straight_flush(self):
        
        return self.has_straight() and self.has_flush()
    
    def classify(self):
        
        if self.has_straight_flush() == True:
            label = 'straight flush'
        elif self.has_four_kind() == True:
            label = 'four of a kind'
        elif self.has_full_house() == True:
            label = 'full house'
        elif self.has_flush() == True:
            label = 'flush'
        elif self.has_straight() == True:
            label = 'straight'
        elif self.has_three_kind() == True:
            label = 'three of a kind'
        elif self.has_two_pair() == True:
            label = 'two pair'
        elif self.has_pair() == True:
            label = 'one pair'
        else:
            label = 'high card'

        return label

class PokerDeck(Deck):

    def deal_hands(self, num_cards=5, num_hands=10):
        hands = []

        for i in range(num_hands):
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)

        return hands

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        
        print(hand)
        print(f"Classification: {hand.classify()}")
        print(f"Does this hand have a pair? {hand.has_pair()}")
        print(f"Does this hand have two pairs? {hand.has_two_pair()}")
        print(f"Does this hand have three of a kind? {hand.has_three_kind()}")
        print(f"Does this hand have four of a kind? {hand.has_four_kind()}")
        print(f"Is this hand a full house? {hand.has_full_house()}")
        print(f"Is this hand a straight? {hand.has_straight()}")
        print(f"Is this hand a flush? {hand.has_flush()}")
        print(f"Is this hand a straight flush? {hand.has_straight_flush()}")
        print('')

# from the solution

def main():
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print(total, 'hands dealt:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0: 
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))

        
if __name__ == '__main__':
    main()