from pure_word_grid import check_if_invalid
from pure_word_grid import build_word_grid

INVALID = 'Sorry that is invalid'

def test_user_input_invalid_none():
    compare_user_input_to_expected_result(None)

def test_user_input_invalid_empty_string():
    compare_user_input_to_expected_result('')

def test_user_input_invalid_integer():
    compare_user_input_to_expected_result(7)

def test_user_input_invalid_list():
    compare_user_input_to_expected_result([])

def test_user_input_invalid_numbers_and_letters():
    compare_user_input_to_expected_result('123abc')

def test_user_input_valid():
    compare_user_input_to_expected_result('pot', None)
    
def compare_user_input_to_expected_result(user_input, output=INVALID):
    result = check_if_invalid(user_input)
    assert result == output

def test_second_letter_is_upper():
    result = build_word_grid('pot')
    assert result == ['Pot', 'pOt', 'poT']