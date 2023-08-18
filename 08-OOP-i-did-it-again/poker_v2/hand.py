from card import Card
from rank import Rank
from typing import List, Dict

class Hand:
    def __init__(self, hand: str) -> None: # 'AS 10S 5H 7C 6S'
        self.hand = self._check_valid(hand) # ['10S', '5H', '6S', '7C', 'AS']
        self.cards = sorted([Card(card) for card in self.hand]) # ['5H', '6S', '7C', '10S', 'AS']
        self.hand_data = self._get_hand_data()
        self.poker_hand, self.placement = self._check_poker_hand()

    def _check_valid(self, hand: str) -> List[str]:
        if not isinstance(hand, str):
            raise TypeError('Sorry, that is an invalid type. It should be of type string.')
        cards_list = sorted(hand.split())
        if len(cards_list) != 5:
            raise ValueError('Sorry, that is not a valid hand. You need to enter 5 cards.')
        for i in range(len(cards_list)-1):
            if cards_list[i] == cards_list[i+1]:
                raise ValueError('Sorry, there are duplicate cards in your hand.')
        return cards_list
    
    # def __gt__(self, other: object) -> bool:
    #     if isinstance(other, Hand):
    #         if self.placement == other.placement:
    #             if self._tie_breaker(other) == self:
    #                 return True
    #             return False
    #         return self.placement > other.placement
    #     else:
    #         raise NotImplementedError()

    # def __gt__(self, other: object) -> bool:
    #     if isinstance(other, Hand):
    #         if self.placement == other.placement:
    #             return self._tie_breaker(other) > other._tie_breaker(self)
    #         return self.placement > other.placement
    #     else:
    #         raise NotImplementedError()

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Hand):
            if self.placement == other.placement:
                return self._tie_breaker(other)
            return self.placement > other.placement
        else:
            raise NotImplementedError()

    def _get_hand_data(self) -> Dict[Rank, List[Card]]:
        ranks_dict: Dict[Rank, List[Card]] = {} # {'6': ['6H', '6C'], '2': ['2D'], 'J': ['JS', 'JD']}
        for card in self.cards:
            if card.rank not in ranks_dict:
                ranks_dict[card.rank] = []
            ranks_dict[card.rank].append(card)
        return ranks_dict

    def _check_poker_hand(self) -> 'tuple[str, int]':
        CHECKS = (
            (self._check_four_of_a_kind, 'Four Of A Kind', 8),
            (self._check_full_house, 'Full House', 7),
            (self._check_three_of_a_kind, 'Three Of A Kind', 4),
            (self._check_two_pair, 'Two Pair', 3),
            (self._check_one_pair, 'One Pair', 2),
            (self._check_royal_flush, 'Royal Flush', 10),
            (self._check_straight_flush, 'Straight Flush', 9),
            (self._check_straight, 'Straight', 5),
            (self._check_flush, 'Flush', 6),
            )
        
        for check, hand, placement in CHECKS:
            if check():
                return hand, placement
        return ('High Card', 1)
    
    def _check_n_of_a_kind(self, n: int) -> bool:
        return any([len(cards) == n for cards in self.hand_data.values()])

    def _check_four_of_a_kind(self) -> bool:
        return self._check_n_of_a_kind(4)
                    
    def _check_full_house(self) -> bool:
        return self._check_three_of_a_kind() and self._check_one_pair()
    
    def _check_three_of_a_kind(self) -> bool:
        return self._check_n_of_a_kind(3)

    def _check_two_pair(self) -> bool:
        return len(self.hand_data) == 3
            
    def _check_one_pair(self) -> bool:
        return self._check_n_of_a_kind(2)

    def _check_royal_flush(self) -> bool:
        return ((self.cards[0].rank == Rank('10') and self.cards[1].rank == Rank('J') and
            self.cards[2].rank == Rank('Q') and self.cards[3].rank == Rank('K') and
            self.cards[4].rank == Rank('A')) and self._check_flush())
   
    def _check_straight_flush(self) -> bool:
        return self._check_straight() and self._check_flush()
   
    def _check_straight(self) -> bool:
        return (all([self.cards[i+1].rank - self.cards[i].rank == 1 for i in range(len(self.cards)-1)]) or
            (self.cards[0].rank == Rank('2') and self.cards[1].rank == Rank('3') and
            self.cards[2].rank == Rank('4') and self.cards[3].rank == Rank('5') and
            self.cards[4].rank == Rank('A')))
    
    def _check_flush(self) -> bool:
        return all([self.cards[i].suit == self.cards[i+1].suit for i in range(len(self.cards)-1)])
    
    def _tie_breaker(self, other: 'Hand') -> bool:
        TIE_CHECKS = {
            8: self._four_of_a_kind_tie_breaker,
            7: self._full_house_tie_breaker,
            4: self._three_of_a_kind_tie_breaker,
            # 3: self._two_pair_tie_breaker,
            2: self._one_pair_tie_breaker,
            # 10: self._royal_flush_tie_breaker,
            # 9: self._straight_flush_tie_breaker,
            # 5: self._straight_tie_breaker,
            # 6: self._flush_tie_breaker,
        }

        t_check = TIE_CHECKS[self.placement]
        return t_check(other)

    def _get_n_of_a_kind(self, n: int) -> Rank:
        for rank, card_list in self.hand_data.items():
            if len(card_list) == n:
                return rank
        raise ValueError(f'There are no ranks with a len of {n}')

    def _four_of_a_kind_tie_breaker(self, other: 'Hand') -> bool:
        return self._get_n_of_a_kind(4) > other._get_n_of_a_kind(4)

    def _one_pair_tie_breaker(self, other: 'Hand') -> bool:
        return self._get_n_of_a_kind(2) > other._get_n_of_a_kind(2)
    
    def _three_of_a_kind_tie_breaker(self, other: 'Hand') -> bool:
        return self._get_n_of_a_kind(3) > other._get_n_of_a_kind(3)
        
    def _full_house_tie_breaker(self, other: 'Hand') -> bool: # Double check the rules of full house tie breaker
        return self._three_of_a_kind_tie_breaker(other)