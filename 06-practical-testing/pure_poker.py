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
            
def get_poker_description(user_input):
    card_list = []
    count_dict = {}
    for c in user_input.split():
        card = parse_card(c)
        card_list.append(card)
    rank_list = []
    for card in card_list:
        rank_list.append(card['rank'])
    for rank in rank_list:
        count_dict[rank] = rank_list.count(rank)
    if 4 in count_dict.values():
        return 'Four Of A Kind'
    elif 3 in count_dict.values() and 2 in count_dict.values():
        return 'Full House'
    elif 3 in count_dict.values():
        return 'Three Of A Kind'
    else:
        count = 0
        for v in count_dict.values():
            if v == 2:
                count += 1
        if count == 1:
            return 'One Pair'
        elif count == 2:
            return 'Two Pair'
        else:
            return 'High Card'
    