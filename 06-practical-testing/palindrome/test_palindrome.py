from pure_palindrome import check_if_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome

INVALID_INPUT = 'Sorry, that is invalid input'


def test_invalid_none():
    compare_input_to_expected_output(None)

def test_invalid_empty_string():
    compare_input_to_expected_output('')

def test_invalid_integer():
    compare_input_to_expected_output(7)

def test_invalid_list():
    compare_input_to_expected_output([])

def test_clean_punctuation():
    result = clean_user_input('a:a')
    assert result == 'aa'

def test_clean_different_punctuation():
    result = clean_user_input('a,a')
    assert result == 'aa'

def test_clean_spaces():
    result = clean_user_input('a a')
    assert result == 'aa'

def test_is_not_palindrome():
    result = check_for_palindrome('pie')
    assert result == 'Not a palindrome'

def test_is_palindrome():
    result = check_for_palindrome('pip')
    assert result == 'Is palindrome'

def test_is_palindrome_extended():
    result = check_for_palindrome('evacaniseebeesinacave')
    assert result == 'Is palindrome'

def test_is_palindrome_capitals():
    result = clean_user_input('Eva, can I see bees in a cave?')
    assert result == 'evacaniseebeesinacave'

def compare_input_to_expected_output(user_input, output=INVALID_INPUT):
    result = check_if_invalid(user_input)
    assert result == output