from suit import Suit
from rank import Rank

class Card:
    def __init__(self, card) -> None:
        self.card = self._check_valid(card)
        self.suit = Suit(self.card[-1])
        self.rank = Rank(self.card[:-1])

    def _check_valid(self, card):
        if not isinstance(card, str):
            raise TypeError('Sorry, that is invalid input. A string is required')
        elif card == '':
            raise ValueError('Sorry, that is not a valid card')
        return card
    
    def __gt__(self, other: object) -> bool:
        return self.rank > other.rank
