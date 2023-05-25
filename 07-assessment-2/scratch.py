from cards.pure_cards import check_for_invalid


def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid
    else:
        card_list = user_input.splite()
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
    list_1 = [card for card in card_list if card[:-1] == card[:-1]+1 for i in range(len(card_list)-1)] # ['2H', '3H', '4H']
    ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in list_1] # [2, 3, 4]
    # number_ranks = [rank for rank in ranks_list if isinstance(rank, int)]
    return len([rank for rank in ranks_list if sorted(ranks_list) == list(range(min(ranks_list), max(ranks_list)+1))]) >= 3


def check_for_4_of_a_kind(card_list):
    return len([rank for rank in number_ranks if sorted(number_ranks) == list(range(min(number_ranks), max(number_ranks)+1))]) >= 4
