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

# def test_card_has_numbered_rank():
#     rank = Card('5H')._rank
#     assert rank == 5

# def test_card_has_letter_rank():
#     rank = Card('AH')._rank
#     assert rank == 'A'

def test_card_has_suit():
    suit = Card('5H')._suit
    assert suit == 'H'

def test_carlas_idea():
    card1 = Card('5H')
    card2 = Card('4C')
    assert card2._rank < card1._rank

def test_dans_idea_greater_than():
    card1 = Card('5H')
    card2 = Card('4C')
    assert card2 < card1

def test_greater_than_letter():
    card1 = Card('KH')
    card2 = Card('6C')
    assert card2 < card1

def test_less_than_number():
    card1 = Card('4C')
    card2 = Card('5H')
    assert card2 > card1

def test_minus_numbers():
    card1 = Card('4C')
    card2 = Card('5H')
    result = card2 - card1
    assert result == 1

def test_minus_letters():
    card1 = Card('10C')
    card2 = Card('QH')
    result = card2 - card1
    assert result == 2

def test_minus_False():
    card1 = Card('6C')
    card2 = Card('8H')
    result = card2 - card1
    assert result != 1