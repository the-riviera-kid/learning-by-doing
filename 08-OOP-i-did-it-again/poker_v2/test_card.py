from card import Card
import pytest

def test_card_exists():
    assert Card

def test_invalid_card_none():
    with pytest.raises(TypeError):
        Card(None)

def test_invalid_card_int():
    with pytest.raises(TypeError):
        Card(13)

def test_invalid_card_list():
    with pytest.raises(TypeError):
        Card([])

def test_invalid_card_dict():
    with pytest.raises(TypeError):
        Card({})

def test_invalid_card_empty_string():
    with pytest.raises(ValueError):
        Card('')

def test_invalid_card_suit():
    with pytest.raises(ValueError):
        Card('4G')

def test_invalid_card_rank():
    with pytest.raises(ValueError):
        Card('1D')

def test_invalid_card_suit_and_rank():
    with pytest.raises(ValueError):
        Card('1000BDF')

def test_valid_card():
    card = Card('2D')
    assert card.card == '2D'

def test_card_greater_than_other():
    assert Card('KH') > Card('QD')

def test_card_less_than_other():
    assert Card('2S') < Card('3C')
