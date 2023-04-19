'''
    pure_poker.py contains only pure functions.
    pure_poker.py cannot at any point during development contain the following statements or functions:
    - print
    - input
    - open

    pure_poker.py can contain the following:
    - indexing
    - imports of any modules

    You may have as many pure modules or test modules as you like
'''
from card import parse_card

def check_hand_is_valid(user_input):
    if user_input == None or user_input == '' or len(user_input.split()) != 5:
        return "Sorry, that's invalid"
    else:
        for c in user_input.split():
            try:
                parse_card(c)
            except ValueError:
                return "Sorry, that's invalid"
        return False
            
            
def get_poker_description(user_input): # '10H JH QC KD AS'
    card_list = get_card_data(user_input)
    rank_list, suit_list, card = get_data(card_list)
    count_dict = get_count_dict(rank_list)
    poker_hand = check_ranks(count_dict, rank_list, suit_list, card)
    return poker_hand
    

def get_card_data(user_input):
    card_list = []
    for c in user_input.split():
        card = parse_card(c)
        card_list.append(card)
    return card_list

def get_data(card_list):
    rank_list = []
    suit_list = []
    for card in card_list:
        rank_list.append(card['rank'])
        suit_list.append(card['suit'])
    return rank_list, suit_list, card

def get_count_dict(rank_list):
    count_dict = {}
    for rank in rank_list:
        count_dict[rank] = rank_list.count(rank)
    return count_dict # {'10': 1, 'jack': 1, 'queen': 1, 'king': 1, 'ace': 1}


def check_ranks(count_dict, rank_list, suit_list, card):
    if 4 in count_dict.values():
        return 'Four Of A Kind'
    elif 3 in count_dict.values() and 2 in count_dict.values():
        return 'Full House'
    elif 3 in count_dict.values():
        return 'Three Of A Kind'
    elif 2 in count_dict.values():
        poker_hand = check_count(count_dict)
        return poker_hand
    
    elif 1 in count_dict.values():
        rank_list_numbers = [int(rank) for rank in rank_list if rank.isnumeric()]
        rank_list_other = [rank for rank in rank_list if not rank.isnumeric()]
        suites = suit_list.count(card['suit'])
        
        if sorted(rank_list_numbers) == sorted(list(range(min(rank_list_numbers), max(rank_list_numbers)+1))) and suites == 5:
            return 'Straight Flush'
        elif suites == 5:
            return 'Flush'
        elif sorted(rank_list_numbers) == sorted(list(range(min(rank_list_numbers), max(rank_list_numbers)+1))):
            if len(rank_list_numbers) == 5:
                return 'Straight'
            elif len(rank_list_numbers) == 4 and 'jack' in rank_list_other or 'ace' in rank_list_other:
                return 'Straight'
            elif len(rank_list_numbers) == 3 and 'jack' in rank_list_other and 'queen' in rank_list_other:
                return 'Straight'
            elif len(rank_list_numbers) == 2 and 'jack' in rank_list_other and 'queen' in rank_list_other and 'king' in rank_list_other:
                return 'Straight'
            elif len(rank_list_numbers) == 1 and 'jack' in rank_list_other and 'queen' in rank_list_other and 'king' in rank_list_other and 'ace' in rank_list_other:
                return 'Straight'
    
    return 'High Card'

def check_count(count_dict):
    count = 0
    for v in count_dict.values():
        if v == 2:
            count += 1
    if count == 1:
        return 'One Pair'
    elif count == 2:
        return 'Two Pair'