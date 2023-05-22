from pure_rummy import rummy


INVALID = 'Sorry, that is invalid'

def test_input_invalid_none():
    compare_input_with_expected_output(None)

def test_input_invalid_empty_string():
    compare_input_with_expected_output('')

def test_input_invalid_integer():
    compare_input_with_expected_output(5)

def test_input_invalid_list():
    compare_input_with_expected_output([])

def test_input_invalid_not_seven_cards():
    compare_input_with_expected_output('2H 3D 4S 5H 4H JC')


def compare_input_with_expected_output(user_input, output=INVALID):
    result = rummy(user_input)
    assert result == output