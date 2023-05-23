from cards.pure_cards import check_for_invalid


def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid
    else:
        ranks_list = [int(i[:-1]) if i[:-1].isnumeric() else i[:-1] for i in user_input.split()]
        return check_rummy(ranks_list)


def check_valid(user_input):
    if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    else:
        for card in user_input.split():
            check_invalid = check_for_invalid(card)
            if check_invalid is not None:
                return check_invalid


def check_rummy(ranks_list):
    game_status = 'Sorry, you lose'
    checks = (
        (check_for_3_of_a_kind),
        (check_for_4_of_a_kind),
    )

    two_wins = [True for check_function in checks if check_function(ranks_list)]
    if len(two_wins) >= 2:
        game_status = 'You Win!'
    return game_status


def check_for_3_of_a_kind(ranks_list):
    return len([rank for rank in ranks_list if sorted(ranks_list) == list(range(min(ranks_list), max(ranks_list)+1))]) >= 3


def check_for_4_of_a_kind(ranks_list):
    return len([rank for rank in ranks_list if sorted(ranks_list) == list(range(min(ranks_list), max(ranks_list)+1))]) >= 4
