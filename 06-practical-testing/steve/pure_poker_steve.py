def description_poker_hand(user_input):                                             # 'KH AH 2C 3D 4S'
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 14:
        return 'Invalid Input'
    suits_list = [i[-1] for i in user_input.split()]                                # ranks_list = ['H', 'H', 'C', 'D', 'S']
    ranks_list = [i[:-1] for i in user_input.split()]                               # ranks_list = ['K', 'A', '2', '3', '4']
    return return_card_function(ranks_list, suits_list)

def calculate_frequencies(ranks_list):
    frequency_ranks = {}
    for rank in ranks_list:
        if rank not in frequency_ranks:
            frequency_ranks[rank] = 0                                               # frequency_ranks = {'K': 0, 'A': 0, '2': 0, '3': 0, '4': 0}
        frequency_ranks[rank] += 1            
    return frequency_ranks
    

def return_card_function(ranks_list, suits_list):
    return_card = None
    frequency_ranks = calculate_frequencies(ranks_list)                             # frequency_ranks = {'K': 1, 'A': 1, '2': 1, '3': 1, '4': 1}
    number_of_ranks = len(frequency_ranks)                                          # number_of_ranks = 5
    frequency_rank_values = frequency_ranks.values()                                # frequency_rank_values = [1, 1, 1, 1, 1]
    ranks = [int(ranks) for ranks in frequency_ranks.keys() if ranks.isnumeric()]   # ranks = [2, 3, 4]
    checks = ((check_for_full_house, 'Full House'),
              (check_for_four_of_a_kind, 'Four of a Kind'),
              (check_for_three_of_a_kind, 'Three of a Kind'),
              (check_for_two_pair, 'Two Pair'),
              (check_for_one_pair, 'One Pair'),
              (check_for_royal_flush, 'Royal Flush'),
              (check_for_straight_flush, 'Straight Flush'),
              (check_for_straight, 'Straight'),
              (check_for_flush, 'Flush'),
              (check_for_high_card, 'High Card'))
    
    for check_function, value in checks:
        if check_function(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
            return_card = value
            break
    return return_card

def check_for_full_house(number_of_ranks, frequency_ranks, frequency_rank_valuesp, suits_list, ranks, ranks_list):
    frequencies = calculate_frequencies(ranks_list)
    frequency_rank_values = frequencies.values()
    return len(frequencies) == 2 and 3 in frequency_rank_values and 2 in frequency_rank_values

def check_for_four_of_a_kind(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return number_of_ranks == 2 and 4 in frequency_rank_values

def check_for_three_of_a_kind(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return number_of_ranks == 3 and 3 in frequency_rank_values

def check_for_two_pair(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    frequencies = calculate_frequencies(ranks_list)
    return len(frequencies) == 3

def check_for_one_pair(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    frequencies = calculate_frequencies(ranks_list)
    return len(frequencies) == 4

def check_for_royal_flush(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return number_of_ranks == 5 and ranks == [10] and all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])

def check_for_straight_flush(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return number_of_ranks == 5 and sorted(ranks) == list(range(min(ranks), max(ranks)+1)) and all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])

def check_for_straight(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):                 # ranks = [2, 3, 4]
    return number_of_ranks == 5 and sorted(ranks) == list(range(min(ranks), max(ranks)+1)) and len(ranks) > 3 or ranks == [10]  # 'KH AH 2C 3D 4S'

def check_for_flush(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])

def check_for_high_card(number_of_ranks, frequency_ranks, frequency_rank_values, suits_list, ranks, ranks_list):
    return True