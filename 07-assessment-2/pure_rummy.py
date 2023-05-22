from cards.pure_cards import check_for_invalid

def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid
    else:
        return check_rummy()


def check_valid(user_input):
    if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    else:
        for card in user_input.split():
            check_invalid = check_for_invalid(card)
            if check_invalid is not None:
                return check_invalid


def check_rummy():
    game_status = None
    checks = (
        (check_for_lose, 'Sorry, you lose'),
    )

    for check_function, message in checks:
        if check_function():
            game_status = message
            break

    return game_status


def check_for_lose():
    return True