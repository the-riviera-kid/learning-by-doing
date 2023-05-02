from random import randint


def get_random_number():
    target_number = randint(1, 101)
    return target_number


def get_error_message_or_none(user_input):
    if user_input is None or not isinstance(user_input, str) or (isinstance(user_input, str) and not user_input.isnumeric()):
        return 'Sorry, your guess is invalid.'
    if int(user_input) < 1 or int(user_input) > 100:
        return 'Your guess should be between 1 and 100'
    return None


def get_game_state(user_input, target_number):
    winner = _did_they_win(user_input, target_number)
    play_game = not winner
    too_low = _is_it_too_low(user_input, target_number)
    message = _get_message(winner, too_low)
    return message, play_game


def _did_they_win(user_input, target_number):
    return int(user_input) == target_number


def _is_it_too_low(user_input, target_number):
    return int(user_input) < target_number


def _get_message(winner, too_low):
    if winner:
        return 'You Win!'
    elif too_low:
        return 'Too low'
    return 'Too high'