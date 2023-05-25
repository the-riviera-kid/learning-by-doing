# from cards.pure_cards import check_for_invalid


# def rummy(user_input):
#     invalid = check_valid(user_input)
#     if invalid is not None:
#         return invalid
#     else:
#         ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in user_input.split()]
#         suits_list = [i[-1] for i in user_input.split()]
#         return check_rummy(ranks_list, suits_list)


# def check_valid(user_input):
#     if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
#         return 'Sorry, that is invalid'
#     else:
#         for card in user_input.split():
#             check_invalid = check_for_invalid(card)
#             if check_invalid is not None:
#                 return check_invalid


# def check_rummy(ranks_list, suits_list):
#     game_status = 'Sorry, you lose'
#     frequency_ranks = calculate_frequencies(ranks_list)
#     number_ranks = [rank for rank in ranks_list if isinstance(rank, int)]
#     checks = (
#         (check_for_3_of_a_kind),
#         (check_for_4_of_a_kind),
#     )

#     two_wins = [True for check_function in checks if check_function(ranks_list, number_ranks, suits_list, frequency_ranks)]
#     if len(two_wins) >= 2:
#         game_status = 'You Win!'
#     return game_status


# def calculate_frequencies(ranks_list): # ranks_list = ['3', '5', '6', '9', '2', '4', '7']
#     frequency_ranks = {}
#     for rank in ranks_list:
#         if rank not in frequency_ranks:
#             frequency_ranks[rank] = 0 # frequency_ranks = {'3': 0, '5': 0, '6': 0, '9': 0, '2': 0, '4': 0, '7': 0}
#         frequency_ranks[rank] += 1 # frequency_ranks = {'3': 1, '5': 1, '6': 1, '9': 1, '2': 1, '4': 1, '7': 1}         
#     return frequency_ranks


# def check_for_3_of_a_kind(ranks_list, number_ranks, suits_list, frequency_ranks):
#     return len([rank for rank in number_ranks if sorted(number_ranks) == list(range(min(number_ranks), max(number_ranks)+1))]) >= 3 and all([suits_list[i] == suits_list[i+1] for i in range(len(suits_list)-1)])


# def check_for_4_of_a_kind(ranks_list, number_ranks, suits_list, frequency_ranks):
#     return len([rank for rank in number_ranks if sorted(number_ranks) == list(range(min(number_ranks), max(number_ranks)+1))]) >= 4



from cards.pure_cards import check_for_invalid


def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid
    else:
        card_list = user_input.split()
        ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in user_input.split()]
        suits_list = [i[-1] for i in user_input.split()]
        return check_rummy(card_list)


def check_valid(user_input):
    if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    else:
        for card in user_input.split():
            check_invalid = check_for_invalid(card)
            if check_invalid is not None:
                return check_invalid


def check_rummy(card_list): # ['2H', '3H', '4H', '5C', '6D', '7S', '8D']
    game_status = 'Sorry, you lose'
    # number_ranks = [rank for rank in ranks_list if isinstance(rank, int)]
    checks = (
        (check_for_3_of_a_kind),
        (check_for_4_of_a_kind),
    )

    two_wins = [True for check_function in checks if check_function(card_list)]
    if len(two_wins) >= 2:
        game_status = 'You Win!'
    return game_status


def check_for_3_of_a_kind(card_list):
    list_1 = [card_list[card] for card in range(len(card_list)-1) if card_list[card][-1] == card_list[card+1][-1]] # ['2H', '3H', '4H']
    print(list_1)
    ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in list_1] # [2, 3, 4]
    print(ranks_list)
    number_ranks = [rank for rank in ranks_list if isinstance(rank, int)]
    return len([rank for rank in number_ranks if sorted(number_ranks) == list(range(min(number_ranks), max(number_ranks)+1))]) >= 3


def check_for_4_of_a_kind(card_list):
    list_1 = [card_list[card] for card in range(len(card_list)-1) if card_list[card][-1] == card_list[card+1][-1]] # ['2H', '3H', '4H']
    print(list_1)
    ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in list_1] # [2, 3, 4]
    print(ranks_list)
    number_ranks = [rank for rank in ranks_list if isinstance(rank, int)]
    return len([rank for rank in number_ranks if sorted(number_ranks) == list(range(min(number_ranks), max(number_ranks)+1))]) >= 4