def parse_card(shorthand):
    if not shorthand or not isinstance(shorthand, str):
        raise ValueError('No valid input argument was provided')
    rank = shorthand[0]
    rank = shorthand[0:-1] if len(shorthand) == 3 else rank

    face_cards = ['A', 'J', 'Q', 'K']
    suit_lookup = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
    }
    rank_lookup = {
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
    try:
        suit = suit_lookup[shorthand[-1]]
        indefinite_article = 'an' if rank_lookup[rank][0] in 'aeiouh' else 'a'
        description = f'{indefinite_article} {rank_lookup[rank]} of {suit}'
        return {
            'rank': rank_lookup[rank] if rank in face_cards else rank,
            'suit': suit,
            'description': description
        }
    except Exception as ex:
        raise ValueError('No valid input argument was provided.', ex)
