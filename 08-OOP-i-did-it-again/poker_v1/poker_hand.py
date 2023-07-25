from card import Card


class PokerHand:
    def __init__(self, hand):
        self._hand = self._is_hand_valid(hand)
        self._hand = [Card(card) for card in self._hand] # check if each card is valid and make a new list
        # Card(card) is creating an object of the class Card
        # a list of 5 Card objects
        self._ranks = [card._rank for card in self._hand] # ['3', '8', '8', '9', '3'] -> ['3', '8', '9']
        self._rank_counts = {r:self._ranks.count(r) for r in self._ranks}
        self._suits = [card._suit for card in self._hand]

    def _is_hand_valid(self, hand):
        if not isinstance(hand, str) or hand == '' or \
            len(set(hand.split())) != 5:
            raise TypeError('Sorry, your poker hand is invalid')
        return hand.split()

    def get_hand_name(self):
        CHECKS = ((self._check_full_house, 'Full House'),
                  (self._check_four_of_a_kind, 'Four Of A Kind'),
                  (self._check_one_pair, 'One Pair'),
                  (self._check_three_of_a_kind, 'Three Of A Kind'),
                  (self._check_two_pair, 'Two Pair'),
                  (self._check_straight, 'Straight'),
                  (self._check_flush, 'Flush'),
                  (self._check_high_card, 'High Card'),)
        
        for check, hand in CHECKS:
            if check():
                return hand
    
    def _check_full_house(self): # ['4', '4', '4,' '8', '8'] -> ['4', '8']
        for r in self._rank_counts:
            return len(set(self._ranks)) == 2 and self._rank_counts[r] == 3
    
    def _check_four_of_a_kind(self):
        return len(set(self._ranks)) == 2
    
    def _check_one_pair(self):
        return len(set(self._ranks)) == 4

    def _check_three_of_a_kind(self): # ['6', '6', '7', 'J', '6'] -> ['6', '7', 'J']
        for r in self._rank_counts:
            return len(set(self._ranks)) == 3 and self._rank_counts[r] == 3
    
    def _check_two_pair(self):
        return len(set(self._ranks)) == 3
    
    def _check_straight(self):
        if sorted(self._ranks) == ['2', '3', '4', '5', 'A']:
            return True
        sorted_cards = sorted(self._hand)
        for i in range(len(sorted_cards)-1):
            if sorted_cards[i+1] - sorted_cards[i] != 1:
                return False
        return True
    
    def _check_flush(self):
        return len(set(self._suits)) == 1
    
    def _check_straight_flush(self):
        if sorted(self._ranks) == ['2', '3', '4', '5', 'A'] and len(set(self._suits)) == 1:
            return True
        sorted_cards = sorted(self._hand)
        for i in range(len(sorted_cards)-1):
            if sorted_cards[i+1] - sorted_cards[i] != 1:
                return False
        return True

    def _check_high_card(self):
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