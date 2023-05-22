def parse_card(user_input):
    check_invalid = check_for_invalid(user_input)
    if check_invalid is not None:
        return check_invalid
    else:
        get_description = get_card_description(user_input)
        return get_description

def check_for_invalid(user_input):
    ranks_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits_list = ['H', 'D', 'S', 'C']
    if not isinstance(user_input, str) or user_input == '' or user_input[:-1] not in ranks_list or user_input[-1] not in suits_list:
        return 'Sorry, that is invalid'
    return None


def get_card_description(user_input):
    descriptions = {'A': 'ace', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'H': 'hearts', 'D': 'diamonds', 'C': 'clubs', 'S': 'spades'}
    card_dict = {}
    card_dict, rank = get_rank(user_input, card_dict, descriptions)
    card_dict, suit = get_suit(user_input, card_dict, descriptions)
    card_dict = get_description(card_dict, rank, suit, descriptions)
    return card_dict


def get_rank(user_input, card_dict, descriptions):
    rank = user_input[:-1]
    if rank.isnumeric():
        card_dict['rank'] = rank
    else:
        card_dict['rank'] = descriptions[rank]
    return card_dict, rank


def get_suit(user_input, card_dict, descriptions):
    suit = user_input[-1]
    card_dict['suit'] = descriptions[suit]
    return card_dict, suit


def get_description(card_dict, rank, suit, descriptions):
    if rank == 'A' or rank == '8':
        card_dict['description'] = f'an {descriptions[rank]} of {descriptions[suit]}'
    else:
        card_dict['description'] = f'a {descriptions[rank]} of {descriptions[suit]}'
    return card_dict
