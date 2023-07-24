class Rank:
    def __init__(self, rank) -> None:
        self.RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.rank = self._check_valid(rank)

    def _check_valid(self, rank):
        if not isinstance(rank, str):
            raise TypeError('Sorry, that is an invalid type. It should be a string type.')
        elif rank == '' or rank not in self.RANKS:
            raise ValueError('Sorry, that is not a valid rank')
        return rank
    
    def __eq__(self, other: object) -> bool:
        return self.rank == other
    
    def __gt__(self, other: object) -> bool:
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)
        
    def __lt__(self, other: object) -> bool:
        if other.rank == '2':
            self.RANKS.insert(0, 'A')
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)
