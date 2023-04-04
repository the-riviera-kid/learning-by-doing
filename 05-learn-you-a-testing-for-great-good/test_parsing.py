from card import parse_card

def test_card_is_dict():
    result = parse_card('5D')
    assert isinstance(result, dict)

def test_rank_in_dict():
    result = parse_card('5D')
    assert 'rank' in result

def test_rank_value_is_5():
    result = parse_card('5D')
    assert result['rank'] == '5'

def test_rank_value_is_7():
    result = parse_card('7D')
    assert result['rank'] == '7'

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

def test_rank_value_not_number():
    result = parse_card('KD')
    assert result['rank'] == 'king'

# ===========================

def test_suit_in_dict():
    result = parse_card('5D')
    assert 'suit' in result

def test_suit_value_is_diamonds():
    result = parse_card('5D')
    assert result['suit'] == 'diamonds'

def test_suit_value_is_hearts():
    result = parse_card('5H')
    assert result['suit'] == 'hearts'

# ===========================

def test_description_in_dict():
    result = parse_card('5D')
    assert 'description' in result

def test_description_value():
    result = parse_card('5D')
    assert result['description'] == 'a five of diamonds'

def test_description_value():
    result = parse_card('JD')
    assert result['description'] == 'a jack of diamonds'

def test_description_value():
    result = parse_card('AC')
    assert result['description'] == 'an ace of cloves'