SUITS = ['H', 'S', 'C', 'D']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, card):
        self._card = self._is_card_valid(card)
        self._rank = self._card[:-1]
        self._suit = self._card[-1]

    def _is_card_valid(self, card):
        if not isinstance(card, str) or card == '' or \
            len(card) < 2 or len(card) > 3 or \
                card[:-1] not in RANKS or \
                card[-1] not in SUITS:
            raise TypeError('Sorry, that is invalid')
        return card
