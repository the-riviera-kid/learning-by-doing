from suit import Suit
import pytest

def test_suit_exits():
    assert Suit

def check_type_errors(user_input):
    with pytest.raises(TypeError):
        Suit(user_input)

def test_invalid_suit_none():
    check_type_errors(None)

def test_invalid_suit_list():
    check_type_errors([])

def test_invalid_suit_dict():
    check_type_errors({})

def test_invalid_suit_int():
    check_type_errors(3)

def check_value_errors(user_input):
    with pytest.raises(ValueError):
        Suit(user_input)

def test_invalid_suit_empty_string():
    check_value_errors('')

def test_invalid_suit_f():
    check_value_errors('f')

def test_valid_suit():
    suit = Suit('H')
    assert suit.suit == 'H'

def test_valid_suit_D():
    suit = Suit('D')
    assert suit.suit == 'D'

def test_compare_suits():
    assert Suit('D') == Suit('D')
