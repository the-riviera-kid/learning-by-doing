from card import Card
import pytest
from typing import Any


def check_type_errors(user_input: Any) -> None:
    with pytest.raises(TypeError):
        Card(user_input)

def test_invalid_card_none() -> None:
    check_type_errors(None)

def test_invalid_card_int() -> None:
    check_type_errors(13)

def test_invalid_card_list() -> None:
    check_type_errors([])

def test_invalid_card_dict() -> None:
    check_type_errors({})

def check_value_errors(user_input: str) -> None:
    with pytest.raises(ValueError):
        Card(user_input)

def test_invalid_card_empty_string() -> None:
    check_value_errors('')

def test_invalid_card_suit() -> None:
    check_value_errors('4G')

def test_invalid_card_rank() -> None:
    check_value_errors('1D')

def test_invalid_card_suit_and_rank() -> None:
    check_value_errors('1000BDF')

def test_valid_card() -> None:
    card = Card('2D')
    assert card.card == '2D'

def test_card_greater_than_other() -> None:
    assert Card('KH') > Card('QD')

def test_card_less_than_other() -> None:
    assert Card('2S') < Card('3C')
