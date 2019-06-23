"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck
from _ast import Num


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
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        return
    
    def has_pair(self):
        self.rank_hist()
        for rank in self.ranks.values():
            if rank == 2:
                return True
        return False
        
    
    def has_two_pairs(self):
        self.rank_hist()
        num_of_pairs = 0
        #print(self)
        for rank in self.ranks.values():
            if rank == 2:
                num_of_pairs += 1
        if num_of_pairs == 2:
            return True
        return False
    
    def has_three_of_a_kind(self):
        self.rank_hist()
        for rank in self.ranks.values():
            if rank == 3:
                return True
        return False
    
    def has_straight(self):
        all_rank_of_cards = []
        for card in self.cards:
            all_rank_of_cards.append(card.rank)
        
        all_rank_of_cards = list(set(all_rank_of_cards))
        all_rank_of_cards.sort()
        if len(all_rank_of_cards) < 5:
            return False
        if ((all_rank_of_cards[-4:] == [10, 11, 12, 13]) and (all_rank_of_cards[0] == 1)):
            return True
        for x in range (len(all_rank_of_cards) , 4, -1):
            if all_rank_of_cards[x - 1] == (all_rank_of_cards[x - 5] + 4):
                return True
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
    
    def has_full_house(self):
        self.rank_hist()
        #print(self.ranks.values())
        for rank in self.ranks.values():
            if rank == 3:
                for rank in self.ranks.values():
                    if rank == 2:
                        return True
        return False
    
    def has_four_of_a_kind(self):
        self.rank_hist()
        for rank in self.ranks.values():
            if rank == 4:
                return True
        return False
    
    def has_straight_flush(self):
        if self.has_flush() is True:
            if self.has_straight() is True:
                return True
        return False
        
    
    def classify(self):
        if self.has_straight_flush():
            return "Straight flush"
        if self.has_four_of_a_kind():
            return "Four of a kind"
        if self.has_full_house():
            return "Full house"
        if self.has_flush():
            return "Flush"
        if self.has_straight():
            return "Straight"
        if self.has_three_of_a_kind():
            return "Three of a kind"
        if self.has_two_pairs():
            return "Two pairs"
        if self.has_pair():
            return "Pair"
        return "No combinations"
        pass
    @staticmethod
    def probability_of_combinations(deck):
        
        num_of_hands = 0
        dic_of_combinations = {"Straight flush" : 0, "Four of a kind" : 0, "Full house" : 0 , "Flush" : 0, "Straight" : 0, "Three of a kind" : 0, "Two pairs" : 0, "Pair" : 0, "No combinations" : 0}
        for _ in range (60000):
            deck = Deck()
            deck.shuffle()
            
            for i in range(10):
                hand = PokerHand()
                num_of_hands += 1
                deck.move_cards(hand, 5)
                hand.sort()
                """print(hand)
                print(hand.classify())
                print(" ")"""
                dic_of_combinations[hand.classify()] += 1
            
        for key in dic_of_combinations:
            print(key, float(dic_of_combinations[key]/num_of_hands * 100))
        return None


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    
    '''for i in range(5):
        hand = PokerHand()
        deck.move_cards(hand, 10)
        #hand.sort()
        print(hand)
        """
        print(hand.has_flush())
        print(hand.has_pair())"""
        
        print('')
        print(hand.classify())
        print('')'''
    deck = Deck()
    PokerHand.probability_of_combinations(deck)

