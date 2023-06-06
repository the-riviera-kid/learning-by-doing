'''
For this assessment, we'll be scoring card hands again, but this time for Rummy!
In Rummy, the objective is to build a hand of seven cards, containing any two of the following patterns:

    three of a kind: three of any rank.
    four of a kind: four of any rank.
    straight three: a straight of three adjacent cards of the same suit.
    straight four: a straight of four adjacent cards of the same suit.

If we're aiming for a hand of seven cards, then we need one pattern of three, and one pattern of four. 
You can have two of the same sort of pattern; three Jacks and four sixes is a valid hand, for instance. 
In Rummy, aces are always low; AS 2S 3S is a valid straight, but QS KS AS is not.

There's no relative ranking of hands in Rummy like in poker; the first player to get a winning hand wins!

Examples:

    AC AS 5C 8C 6C 7C AH: WIN a straight (continuous sequence) four and three of a kind(3 of one rank - AC AS AH). Note that I haven't written the cards down in order, but it still counts.
    AH 2H 3H 4H 5H 6H 7H: WIN A straight four and a straight three. It doesn't matter which patter contains the 4H, it's valid either way. Notice that two straights are a winning hand; it doesn't have to be 3/4 of a kind and a straight.
    10H 9H 8H 7H 7C 7S 7D: WIN this is ambiguous, it could be a straight three and four of a kind, or it could be a straight four and three of a kind. Either way, this is a winning hand.
    QC KC AC AS 2S 3S 4S: LOSE Aces are low, so A, 2, 3, 4 is a straight, but Q, K, A is not.
    3C 3D 3H 3S 4S 5C 6S: LOSE Straights have to be all the same suit. This is just a four of a kind.
    AH 2H 3H 4H 5H 6H 7H 8H: INVALID Valid hands only have seven cards.
    AH 2H 3H 4B 5H 6H 7H: INVALID 'B' is not a valid suit.
    potatopotato: INVALID It may surprise you that a potato is not a real playing card.

Challenge:
Your task is to write a program which prompts the user for a string representing a Rummy hand, and prints "WIN", "LOSE" or "INVALID" in response. 
You are allowed to copy over your card.py module from a previous exercise, should you choose.

Write tests for as much of your program as possible. The best way to do this is to separate input and output from the processing. 
Remember to check for invalid hands as well as winning and losing hands.

This is an assessment, so you will be working individually. 
Once you're done, make sure your project is committed, and pushed to Github.
'''

from cards.pure_cards import check_for_invalid


def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid
    else:
        card_list = user_input.split()
        return check_rummy(card_list)


def check_valid(user_input):
    if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    else:
        for card in user_input.split():
            check_invalid = check_for_invalid(card)
            if check_invalid is not None:
                return check_invalid


def check_rummy(card_list):
    win_or_lose = 'LOSE'
    frequencies = calculate_frequencies(card_list)
    if check_for_3_of_a_kind(frequencies) and check_for_straight_4(frequencies):
        return 'WIN'
    elif check_for_4_of_a_kind(frequencies) and check_for_straight_3(frequencies):
        return 'WIN'
    return win_or_lose


def calculate_frequencies(card_list): # AC AS 8C 9C JC 10C AH
    frequencies = {}
    for card in card_list: # card_list = ['AC', 'AS', '8C', '9C', 'JC', '10C', 'AH']
        rank = card[:-1]
        suit = card[-1]
        if rank in frequencies:
            frequencies[rank].append(suit)
        else:
            frequencies[rank] = [suit]
    return frequencies


def check_for_3_of_a_kind(frequencies):
    for suits in frequencies.values():
        return len(suits) == 3

def check_for_4_of_a_kind(frequencies):
    for suits in frequencies.values():
        return len(suits) == 4


def check_for_straight_4(frequencies): # {'A': ['C', 'S', 'H'], '8': ['C'], '9': ['C'], 'J': ['C'], '10': ['C']}
    ranks_list = [int(rank) for rank, suits in frequencies.items() if rank.isnumeric() if len(suits) == 1] # ranks_list = [8, 9, 10]
    ranks_list_letters = [rank for rank, suits in frequencies.items() if rank.isalpha() if len(suits) == 1] # ranks_list = ['J']
    suits_list = [suits[0] for suits in frequencies.values() if len(suits) == 1] # suits_list = ['C', 'C', 'C', 'C']
    if len(ranks_list) == 4 or \
       len(ranks_list) == 3 and 'J' in ranks_list_letters or \
       len(ranks_list) == 2 and 'J' in ranks_list_letters and 'Q' in ranks_list_letters or \
       len(ranks_list) == 1 and len(ranks_list_letters) == 3:
        return sorted(ranks_list) == list(range(min(ranks_list), max(ranks_list)+1)) and all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])


def check_for_straight_3(frequencies):
    ranks_list = [int(rank) for rank, suits in frequencies.items() if rank.isnumeric() if len(suits) == 1]
    ranks_list_letters = [rank for rank, suits in frequencies.items() if rank.isalpha() if len(suits) == 1]
    suits_list = [suits[0] for suits in frequencies.values() if len(suits) == 1]
    if len(ranks_list) == 3 or \
       len(ranks_list) == 2 and 'J' in ranks_list_letters or \
       len(ranks_list) == 1 and 'J' in ranks_list_letters and 'Q' in ranks_list_letters:
        return sorted(ranks_list) == list(range(min(ranks_list), max(ranks_list)+1)) and all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])
    return len(ranks_list) == 0 and 'J' in ranks_list_letters and 'Q' in ranks_list_letters and 'K' in ranks_list_letters or \
         len(ranks_list) == 0 and 'Q' in ranks_list_letters and 'K' in ranks_list_letters and 'A' in ranks_list_letters
