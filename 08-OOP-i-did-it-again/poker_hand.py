from card import Card


class PokerHand:
    def __init__(self, hand):
        self._hand = self._is_hand_valid(hand)
        self._hand = [Card(card) for card in self._hand] # check if each card is valid and make a new list
        # Card(card) is creating an object of the class Card
        # a list of 5 Card objects

    def _is_hand_valid(self, hand):
        if not isinstance(hand, str) or hand == '' or \
            len(hand.split()) != 5:
            raise TypeError('Sorry, your poker hand is invalid')
        return hand.split()

    def get_hand_name(self):
        rank = [card._rank for card in self._hand] # ['A', '10', '5', '10', '6']
        if len(set(rank)) == 4:
            return 'One Pair'
        return 'High Card'


'''
CHECKS = ((full_house, 'Full House', 7),
        (four_of_a_kind, 'Four of a Kind', 8),
        (three_of_a_kind, 'Three of a Kind', 4),
        (two_pair, 'Two Pair', 3),
        (one_pair, 'One Pair', 2),
        (royal_flush, 'Royal Flush', 10),
        (straight_flush, 'Straight Flush', 9),
        (straight, 'Straight', 5),
        (flush, 'Flush', 6),
        (high_card, 'High Card', 1))        
'''