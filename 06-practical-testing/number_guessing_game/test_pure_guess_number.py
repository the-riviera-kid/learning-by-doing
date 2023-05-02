from pure_guess_number import get_error_message_or_none
from pure_guess_number import get_game_state


def test_input_invalid_none():
    compare_input_output(None)

def test_input_invalid_list():
    compare_input_output([])

def test_input_invalid_string():
    compare_input_output('h')

def test_input_is_number():
    compare_input_output('6', None)

def test_input_is_too_low():
    compare_input_output('-9')

def test_input_is_too_low_zero():
    compare_input_output('0', 'Your guess should be between 1 and 100')

def test_input_is_too_high():
    compare_input_output('110', 'Your guess should be between 1 and 100')

# =================================

def test_user_wins_2():
    result = get_game_state('8', 8)
    assert result == ('You Win!', False)

def test_guess_too_low_2():
    result = get_game_state('5', 50)
    assert result == ('Too low', True)

def test_guess_too_high_2():
    result = get_game_state('90', 50)
    assert result == ('Too high', True)


# =====================================


def compare_input_output(input, expected_result='Sorry, your guess is invalid.'):
    result = get_error_message_or_none(input)
    assert result == expected_result
