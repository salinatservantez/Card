# Author: Salina Servantez
# Program Descripttion:
# This program prints out n randomly generated
# cards and the associated Blackjack value where n is a number supplied
# by the user.
#

class Card:
    """playing card object where numeric rank, suit and blackjack values are stored"""

    def __init__(self, rank, suit):
        """set the rank, suit and the ranks, as well as the suits"""
        self.rank = rank
        self.suit = suit
        self.ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
                      "Queen", "King"]

        self.suits = {"d": "Diamonds",
                      "c": "Clubs",
                      "h": "Hearts",
                      "s": "Spades"}

    def getRank(self):
        """returns the rank of the card"""
        return self.ranks[self.rank]

    def getSuit(self):
        """returns the suit"""
        return self.suits.get(self.suit)

    def value(self):
        """check if value is between 1 and 11 and then return it's rank, if it is
            equal to 1 return 1 otherwise return 10"""

        if self.rank == 1:
            return 1

        elif self.rank == 11 or self.rank == 12 or self.rank == 13:
            return 10

        else:
            return self.rank

    def __str__(self):
        """return the the rank and suit as a string"""
        return "%s of %s" % (self.getRank(), self.getSuit())
