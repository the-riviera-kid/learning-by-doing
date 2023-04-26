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


def check_hand_is_invalid(user_input):
    if user_input == None or user_input == '' or len(user_input.split()) != 5:
        return True
    else:
        for c in user_input.split():
            try:
                parse_card(c)
            except ValueError:
                return True
        return False
            

def get_poker_description(user_input): # '10H JH QC KD AS'
    count_dict, rank_list_numbers, suites, rank_list_other = get_poker_hand_stats(user_input)
    poker_hand = get_hand_from_stats(count_dict, rank_list_numbers, suites, rank_list_other)
    return poker_hand


def get_poker_hand_stats(user_input):
    card_list = get_card_data(user_input)
    rank_list, suit_list, card = get_data(card_list)
    count_dict = get_count_dict(rank_list)
    rank_list_numbers, rank_list_other, suites = get_rank_lists(suit_list, rank_list, card)
    return count_dict, rank_list_numbers, suites, rank_list_other

     
def get_hand_from_stats(count_dict, rank_list_numbers, suites, rank_list_other):  
    same_kinds = check_same_kinds(count_dict)
    unique_card_hands = check_unique_card_hands(rank_list_numbers, suites)
    straight = check_straight(rank_list_numbers, rank_list_other)
    return same_kinds or unique_card_hands or straight or 'High Card'


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


def get_rank_lists(suit_list, rank_list, card):
    rank_list_numbers = [int(rank) for rank in rank_list if rank.isnumeric()]
    rank_list_other = [rank for rank in rank_list if not rank.isnumeric()]
    suites = suit_list.count(card['suit'])
    return rank_list_numbers, rank_list_other, suites


def check_same_kinds(count_dict):
    if 4 in count_dict.values():
        return 'Four Of A Kind'
    elif 3 in count_dict.values() and 2 in count_dict.values():
        return 'Full House'
    elif 3 in count_dict.values():
        return 'Three Of A Kind'
    elif 2 in count_dict.values():
        poker_hand = check_count(count_dict)
        return poker_hand


def check_count(count_dict):
    count = 0
    for v in count_dict.values():
        if v == 2:
            count += 1
    if count == 1:
        return 'One Pair'
    elif count == 2:
        return 'Two Pair'


def check_unique_card_hands(rank_list_numbers, suites):
    if sorted(rank_list_numbers) == [10] and suites == 5:
        return 'Royal Flush'
    if sorted(rank_list_numbers) == sorted(list(range(min(rank_list_numbers), max(rank_list_numbers)+1))) and suites == 5:
        return 'Straight Flush'
    elif suites == 5:
        return 'Flush'


def check_straight(rank_list_numbers, rank_list_other):
    if sorted(rank_list_numbers) == sorted(list(range(min(rank_list_numbers), max(rank_list_numbers)+1))):
        if len(rank_list_numbers) == 5 or \
            len(rank_list_numbers) == 4 and 'jack' in rank_list_other or 'ace' in rank_list_other or \
            len(rank_list_numbers) == 3 and 'jack' in rank_list_other and 'queen' in rank_list_other or \
            len(rank_list_numbers) == 2 and 'jack' in rank_list_other and 'queen' in rank_list_other and \
                'king' in rank_list_other or \
            len(rank_list_numbers) == 1 and 'jack' in rank_list_other and 'queen' in rank_list_other and \
                'king' in rank_list_other and 'ace' in rank_list_other:
                return 'Straight'
        