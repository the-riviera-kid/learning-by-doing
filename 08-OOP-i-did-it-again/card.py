SUITS = ['H', 'S', 'C', 'D']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, card):
        self._card = self._is_card_valid(card)
        # self._rank = self._check_rank_type(self._card)
        self._rank = self._card[:-1]
        self._suit = self._card[-1]

    def _is_card_valid(self, card):
        if not isinstance(card, str) or card == '' or \
            len(card) < 2 or len(card) > 3 or \
                card[:-1] not in RANKS or \
                card[-1] not in SUITS:
            raise TypeError('Sorry, that is invalid')
        return card

    # def _check_rank_type(self, card):
    #     if card[:-1].isnumeric():
    #         return int(card[:-1])
    #     return card[:-1]
    
    def __gt__(self, other): # 'KH', '4C'
        return RANKS.index(self._rank) > RANKS.index(other._rank)
        
    def __lt__(self, other): # 'KH', '4C'
        return RANKS.index(self._rank) < RANKS.index(other._rank)
        
    def __sub__(self, other): # 'QH', '10C'
        return RANKS.index(self._rank) - RANKS.index(other._rank) # return 10 - 8 -> 10 & 8 are the indexes of 'Q' & '10'