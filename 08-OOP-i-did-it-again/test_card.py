from card import Card
import pytest

def test_Card_exists():
    assert Card('5H')

def test_invalid_card_None():
    with pytest.raises(TypeError):
        Card(None)

def test_invalid_card_int():
    with pytest.raises(TypeError):
        Card(2)

def test_invalid_card_empty_string():
    with pytest.raises(TypeError):
        Card('')

def test_invalid_card_too_short():
    with pytest.raises(TypeError):
        Card('3')

def test_invalid_card_too_long():
    with pytest.raises(TypeError):
        Card('300000')

def test_invalid_card_no_rank():
    with pytest.raises(TypeError):
        Card('1H')

def test_invalid_card_negative():
    with pytest.raises(TypeError):
        Card('-1H')

def test_invalid_card_no_suit():
    with pytest.raises(TypeError):
        Card('30')

def test_card_has_rank():
    rank = Card('5H')._rank
    assert rank == '5'

def test_card_has_suit():
    suit = Card('5H')._suit
    assert suit == 'H'