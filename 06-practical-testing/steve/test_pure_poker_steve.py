from pure_poker_steve import description_poker_hand

INVALID_STRING = 'Invalid Input'

def test_find_function():
    assert description_poker_hand

def test_invalid_input_empty_string():
    helper_function('')

def test_invalid_input_none():
    helper_function(None)

def test_invalid_input_int():
    helper_function(12)

def test_invalid_input_list():
    helper_function([])

def helper_function(data):
    result = description_poker_hand(data)
    assert result == INVALID_STRING