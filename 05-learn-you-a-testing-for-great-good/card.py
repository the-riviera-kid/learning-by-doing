def parse_card(short_description): # 'AD' -> 'an ace of diamonds'
    ranks = {'2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', 'A': 'ace', 'J':'jack', 'Q': 'queen', 'K': 'king'}
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    card = {}
    check_if_valid(short_description)
    rank = set_rank_in_dict_if_letter(short_description, card, ranks) # set key 'rank' in card dict
    card = set_suit_in_dict(short_description, suits, rank, card) # set key 'suit' and 'description' in card dict
    return card # {'rank': 'ace', 'suit': 'diamond', 'description': 'an ace of diamonds'}

def check_if_valid(short_description):
    if not isinstance(short_description, str):
        raise TypeError('Invalid card description, no good for card parsing.')
    if short_description[-1] not in ['H', 'D', 'S', 'C']:
        raise ValueError('Invalid suit in short description for card parsing.')

# set key 'rank' in card dict for letter
def set_rank_in_dict_if_letter(short_description, card, ranks):
    if short_description[0] not in ['A', 'J', 'Q', 'K']:
        rank = set_rank_in_dict_if_number(short_description, card, ranks)
    else:
        for shrt_rank, rank in ranks.items():
            if short_description[0] in shrt_rank:
                card['rank'] = rank          # card = {'rank': 'ace'}
                break
    return rank

# set key 'rank' in card dict for number
def set_rank_in_dict_if_number(short_description, card, ranks):
    if short_description[:-1].isnumeric() == False:
            raise ValueError('Invalid rank for card parsing.')
    else:
        number = int(short_description[:-1])
        if not number >= 2 or not number <= 10:
            raise ValueError('Invalid rank for card parsing.')
        else:
            card['rank'] = short_description[:-1]     # 5D -> card = {'rank': '5'}
            rank = ranks[short_description[:-1]]
    return rank

def set_suit_in_dict(short_description, suits, rank, card):
    for suit in suits:
        if short_description[1].lower() in suit[0]: # AD -> 'd' in 'diamonds'
            card['suit'] = suit
            card = set_description_in_dict(card, rank, suit) # set key 'description' in card dict
    return card # card = {'rank': 'ace', 'suit': 'diamond'}

def set_description_in_dict(card, rank, suit):
    if card['rank'] == 'ace' or card['rank'] == '8':
        card['description'] = f'an {rank} of {suit}'
    else:
        card['description'] = f'a {rank} of {suit}'
    return card