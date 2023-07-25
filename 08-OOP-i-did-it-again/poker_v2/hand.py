from card import Card

class Hand:
    def __init__(self, hand) -> None: # 'AS 10S 5H 7C 6S'
        self.hand = self._check_valid(hand) # ['AS', '10S', '5H', '7C', '6S']
        self.cards = [Card(card) for card in self.hand]
        self.hand_data = self._get_hand_data()

    def _check_valid(self, hand):
        if not isinstance(hand, str):
            raise TypeError('Sorry, that is an invalid type. It should be of type string.')
        sorted_cards = sorted(hand.split())
        if hand == '' or len(sorted_cards) != 5:
            raise ValueError('Sorry, that is not a valid hand. You need to enter 5 cards.')
        for i in range(len(sorted_cards)-1):
            if sorted_cards[i] == sorted_cards[i+1]:
                raise ValueError('Sorry, there are duplicate cards in your hand.')
        return sorted_cards
        
    def _get_hand_data(self):
        ranks_dict = {} # {'6': ['6H', '6C']}
        for card in self.cards:
            if card.rank not in ranks_dict:
                ranks_dict[card.rank] = []
            ranks_dict[card.rank].append(card)
        return ranks_dict
     
    def _check_poker_hand(self):
        CHECKS = (
            (self._check_four_of_a_kind, 'Four Of A Kind'),
            (self._check_three_of_a_kind, 'Three Of A Kind'),
            (self._check_two_pair, 'Two Pair'),
            (self._check_one_pair, 'One Pair'),
            # (self._check_straight, 'Straight'),
            (self._check_high_card, 'High Card'),
            )
        
        for check, hand in CHECKS:
            if check():
                return hand

    def _check_n_of_a_kind(self, n):
        return any([len(cards) == n for cards in self.hand_data.values()])

    def _check_four_of_a_kind(self):
        return self._check_n_of_a_kind(4)
                    
    def _check_three_of_a_kind(self):
        return self._check_n_of_a_kind(3)
            
    def _check_two_pair(self):
        return len(self.hand_data) == 3
        
    def _check_one_pair(self):
        return self._check_n_of_a_kind(2)

    def _check_high_card(self):
        return True
    
