from card import Card


class PokerHand:
    def __init__(self, hand):
        self._hand = self._is_hand_valid(hand)
        for card in self._hand:
            Card(card)

    def _is_hand_valid(self, hand):
        if not isinstance(hand, str) or hand == '' or \
            len(hand.split()) != 5:
            raise TypeError('Sorry, your poker hand is invalid')
        return hand.split()

    def get_hand_name(self):
        return 'High Card'
