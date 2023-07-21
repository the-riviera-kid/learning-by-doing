from suit import Suit
import pytest

def test_suit_exits():
    assert Suit

def test_invalid_suit_none():
    with pytest.raises(TypeError):
        Suit(None)

def test_invalid_suit_empty_string():
    with pytest.raises(ValueError):
        Suit('')

def test_invalid_suit_f():
    with pytest.raises(ValueError):
        Suit('f')

def test_invalid_suit_list():
    with pytest.raises(TypeError):
        Suit([])

def test_invalid_suit_dict():
    with pytest.raises(TypeError):
        Suit({})

def test_invalid_suit_int():
    with pytest.raises(TypeError):
        Suit(3)

def test_valid_suit():
    suit = Suit('H')
    assert suit.suit == 'H'

def test_valid_suit_D():
    suit = Suit('D')
    assert suit.suit == 'D'

def test_compare_suits():
    assert Suit('D') == Suit('D')
