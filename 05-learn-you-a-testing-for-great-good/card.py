def parse_card(short_description):
    ranks = ['ace', 'jack', 'queen', 'king']
    numbers = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'eight', '9': 'nine', '10': 'ten'}
    suits = ['hearts', 'diamonds', 'spades', 'cloves']
    card = {}
    if short_description[0].isnumeric():
        card['rank'] = short_description[0]     # 5D -> card = {'rank': '5'}
        rank = numbers[short_description[0]]
    else:
        for rank in ranks:
            if short_description[0].lower() in rank[0]: # AD -> 'ace' 'diamonds' 'an ace of diamonds'
                card['rank'] = rank                     # card = {'rank': 'ace'}
                break
    for suit in suits:
        if short_description[1].lower() in suit[0]: # AD -> 'd' in 'diamonds'
            card['suit'] = suit                     # card = {'rank': 'ace', 'suit': 'diamond'}
            if card['rank'] == 'ace':
                card['description'] = f'an {rank} of {suit}'
            else:
                card['description'] = f'a {rank} of {suit}'
    return card # {'rank': 'ace', 'suit': 'diamond'}
