def parse_card(short_description):
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    ranks = {'2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', 'A': 'ace', 'J':'jack', 'Q': 'queen', 'K': 'king'}
    card = {}
    if not isinstance(short_description, str):
        raise TypeError('Invalid card description, no good for card parsing.')
    if short_description[-1].lower() not in ['h', 'd', 's', 'c']:
        raise ValueError('Invalid suit in short description for card parsing.')
    if short_description[0].lower() not in ['a', 'j', 'q', 'k']:
        if short_description[:-1].isnumeric() == False:
            raise ValueError('Invalid rank for card parsing.')
        else:
            number = int(short_description[:-1])
            if not number >= 2 or not number <= 10:
                raise ValueError('Invalid rank for card parsing.')
            else:
                card['rank'] = short_description[:-1]     # 5D -> card = {'rank': '5'}
                rank = ranks[short_description[:-1]]
    else:
        for shrt_d, rank in ranks.items():
            if short_description[0] in shrt_d: # AD -> 'ace' 'diamonds' 'an ace of diamonds'
                card['rank'] = rank                  # card = {'rank': 'ace'}
                break
    for suit in suits:
        if short_description[1].lower() in suit[0]: # AD -> 'd' in 'diamonds'
            card['suit'] = suit                     # card = {'rank': 'ace', 'suit': 'diamond'}
            if card['rank'] == 'ace':
                card['description'] = f'an {rank} of {suit}'
            else:
                card['description'] = f'a {rank} of {suit}'
    return card # {'rank': 'ace', 'suit': 'diamond'}
