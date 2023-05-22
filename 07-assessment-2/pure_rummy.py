from cards.pure_cards import parse_card

def rummy(user_input):
    invalid = check_valid(user_input)
    if invalid is not None:
        return invalid


def check_valid(user_input):
    if user_input == '' or not isinstance(user_input, str) or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    else:
        for card in user_input.split():
            parse_card(card)