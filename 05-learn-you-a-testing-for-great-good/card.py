FACE_CARDS = ['A', 'J', 'Q', 'K']
SUIT_LOOKUP = {
    'C': 'clubs',
    'D': 'diamonds',
    'H': 'hearts',
    'S': 'spades',
}
RANK_LOOKUP = {
    'A': 'ace',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    'J': 'jack',
    'Q': 'queen',
    'K': 'king'
}

def parse_card(shorthand):
    if not shorthand or not isinstance(shorthand, str):
        raise ValueError('No valid input argument was provided')

    rank = shorthand[0:-1] if len(shorthand) == 3 else shorthand[0]
    if rank not in RANK_LOOKUP:
        raise ValueError('Invalid rank')

    suit = shorthand[-1]
    if suit not in SUIT_LOOKUP:
        raise ValueError('Invalid suit')

    rank_name = RANK_LOOKUP[rank]
    suit_name = SUIT_LOOKUP[suit]
    short_rank_name = rank_name if rank in FACE_CARDS else rank
    indefinite_article = 'an' if rank_name[0] in 'aeiouh' else 'a'
    description = f'{indefinite_article} {rank_name} of {suit_name}'

    return {
        'rank': short_rank_name,
        'suit': suit_name,
        'description': description
    }

