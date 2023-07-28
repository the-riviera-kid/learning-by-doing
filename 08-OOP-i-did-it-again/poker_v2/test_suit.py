from suit import Suit
import pytest
from typing import Any

def check_type_errors(user_input: Any) -> None:
    with pytest.raises(TypeError):
        Suit(user_input)

def test_invalid_suit_none() -> None:
    check_type_errors(None)

def test_invalid_suit_list() -> None:
    check_type_errors([])

def test_invalid_suit_dict() -> None:
    check_type_errors({})

def test_invalid_suit_int() -> None:
    check_type_errors(3)

def check_value_errors(user_input: str) -> None:
    with pytest.raises(ValueError):
        Suit(user_input)

def test_invalid_suit_empty_string() -> None:
    check_value_errors('')

def test_invalid_suit_f() -> None:
    check_value_errors('f')

def test_valid_suit() -> None:
    suit = Suit('H')
    assert suit.suit == 'H'

def test_valid_suit_D() -> None:
    suit = Suit('D')
    assert suit.suit == 'D'

def test_compare_suits() -> None:
    assert Suit('D') == Suit('D')
