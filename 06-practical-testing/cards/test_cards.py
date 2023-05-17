from pure_cards import parse_card

INVALID = 'Sorry, that is invalid'

def test_user_input_invalid_none():
    compare_input_with_expected_result(None)

def test_user_input_invalid_empty_string():
    compare_input_with_expected_result('')

def test_user_input_invalid_empty_list():
    compare_input_with_expected_result([])

def test_user_input_invalid_integer():
    compare_input_with_expected_result(9)

def test_user_input_invalid_100C():
    compare_input_with_expected_result('100C')

def test_user_input_invalid_C():
    compare_input_with_expected_result('C')

def test_user_input_invalid_C2():
    compare_input_with_expected_result('C2')

def test_user_input_invalid_22():
    compare_input_with_expected_result('22')

def compare_input_with_expected_result(user_input, output=INVALID):
    result = parse_card(user_input)
    assert result == output

# def test_rank_exists_2D():
#     result = parse_card('2D')
#     assert 'rank' in result

# def test_suit_exists_3H():
#     result = parse_card('3H')
#     assert 'suit' in result

# def test_suit_exists_4S():
#     result = parse_card('4S')
#     assert 'description' in result

# ===========

def helper_function(user_input, key):
    result = parse_card(user_input)
    assert key in result

def test_rank_exists_KH():
    helper_function('KH', 'rank')

def test_suit_exists_2D():
    helper_function('2D', 'suit')

def test_description_exists_4S():
    helper_function('4S', 'description')

# ===========

def test_user_input_valid_10C():
    compare_input_with_expected_result('10C', {'rank': '10', 'suit': 'clubs', 'description': 'a ten of clubs'})

def test_user_input_valid_AS_an():
    compare_input_with_expected_result('AS', {'rank': 'ace', 'suit': 'spades', 'description': 'an ace of spades'})

def test_user_input_valid_8S_an():
    compare_input_with_expected_result('8S', {'rank': '8', 'suit': 'spades', 'description': 'an eight of spades'})
