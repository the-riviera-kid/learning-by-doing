import pytest
from card import parse_card

def test_card_is_dict():
    result = parse_card('5D')
    assert isinstance(result, dict)

def test_card_is_dict_invalid_input():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card(None)

def test_card_is_dict_invalid_input_empty_list():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card([])

def test_card_is_dict_invalid_input_list():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card(['A', 'D'])

def test_card_is_dict_invalid_input_empty_dict():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card({})

def test_card_is_dict_invalid_input_empty_dict():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card({1: 'D', 'A': 'S'})

def test_rank_in_dict():
    result = parse_card('5D')
    assert 'rank' in result

def test_rank_value_is_5():
    result = parse_card('5D')
    assert result['rank'] == '5'

def test_rank_value_is_7():
    result = parse_card('7D')
    assert result['rank'] == '7'

def test_rank_value_is_10():
    result = parse_card('10D')
    assert result['rank'] == '10'

def test_rank_value_is_11():
    with pytest.raises(ValueError, match='Invalid rank'):
        parse_card('11C')

def test_rank_value_is_lower_case():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card('aH')

def test_suit_is_lower_case():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card('5h')

def test_input_is_invalid_characters():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card(';...:')

def test_rank_value_is_negative_2():
    with pytest.raises(ValueError, match='Invalid rank'):
        parse_card('-2H')

def test_rank_value_is_negative_too_long():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card('2AAAAH')

def test_input_is_integer():
    with pytest.raises(TypeError, match='card parsing'):
        parse_card(2)

def test_rank_value_is_ace():
    result = parse_card('AD')
    assert result['rank'] == 'ace'

def test_rank_value_is_jack():
    result = parse_card('JD')
    assert result['rank'] == 'jack'

def test_rank_value_is_queen():
    result = parse_card('QD')
    assert result['rank'] == 'queen'
    
def test_rank_value_is_king():
    result = parse_card('KD')
    assert result['rank'] == 'king'

# ===========================

def test_suit_value_is_valid():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card('4U')

def test_suit_in_dict():
    result = parse_card('5D')
    assert 'suit' in result

def test_suit_value_is_diamonds():
    result = parse_card('5D')
    assert result['suit'] == 'diamonds'

def test_suit_value_is_hearts():
    result = parse_card('5H')
    assert result['suit'] == 'hearts'

def test_suit_is_lower_case():
    with pytest.raises(ValueError, match='card parsing'):
        parse_card('5h')

# ===========================

def test_description_in_dict():
    result = parse_card('8C')
    assert 'description' in result

def test_description_value_five():
    result = parse_card('5D')
    assert result['description'] == 'a five of diamonds'


def test_description_value_jack():
    result = parse_card('JD')
    assert result['description'] == 'a jack of diamonds'

def test_description_value_ace():
    result = parse_card('AC')
    assert result['description'] == 'an ace of clubs'

def test_description_value_eight():
    result = parse_card('8H')
    assert result['description'] == 'an eight of hearts'
