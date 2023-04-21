from pure_poker import check_hand_is_invalid
from pure_poker import get_poker_data
from pure_poker import get_poker_description

def test_poker_input_none():
    result = check_hand_is_invalid(None)
    assert result == True

def test_poker_input_empty_string():
    result = check_hand_is_invalid('')
    assert result == True

def test_poker_one_card():
    result = check_hand_is_invalid('5H')
    assert result == True

def test_poker_invalid_card():
    result = check_hand_is_invalid('5C 10D 7H AS 44C')
    assert result == True

def test_poker_valid_card():
    result = check_hand_is_invalid('5C 2D 7H AS 4C')
    assert result == False

def test_poker_high_card():
    result = get_poker_data('5C 2D 7H AS 4C')
    assert result == 'High Card'

# Separating the function means more tests and slowly deprecating old tests
def test_poker_high_card_description():
    result = get_poker_description('....') # different input
    assert result == '....' # different result


def test_poker_high_card_mixed_numbers_others():
    result = get_poker_data('KD 8C 10S 9S 7D')
    assert result == 'High Card'

def test_poker_one_pair():
    result = get_poker_data('AS 10S 5H 10C 6S')
    assert result == 'One Pair'

def test_poker_two_pair():
    result = get_poker_data('3H 8C 8H 9S 3D')
    assert result == 'Two Pair'

def test_poker_three_of_a_kind():
    result = get_poker_data('6S 6H 7C JD 6D')
    assert result == 'Three Of A Kind'

def test_poker_full_house():
    result = get_poker_data('4H 4D 4C 8S 8D')
    assert result == 'Full House'

def test_poker_four_of_a_kind():
    result = get_poker_data('JC JD JS JC 5H')
    assert result == 'Four Of A Kind'

def test_poker_straight_only_numbers():
    result = get_poker_data('2H 3C 4S 5H 6D')
    assert result == 'Straight'

def test_poker_straight_mixed_numbers():
    result = get_poker_data('6D 8C 10S 9S 7D')
    assert result == 'Straight'

def test_poker_straight_with_jack():
    result = get_poker_data('JD 8C 10S 9S 7D')
    assert result == 'Straight'

def test_poker_straight_with_ace():
    result = get_poker_data('AS 2H 3C 4S 5D')
    assert result == 'Straight'

def test_poker_straight_with_queen():
    result = get_poker_data('9S 10H JH 8C QC')
    assert result == 'Straight'

def test_poker_straight_with_king():
    result = get_poker_data('10H JH QC KD 9S')
    assert result == 'Straight'

def test_poker_straight_with_king_and_ace():
    result = get_poker_data('10H JH QC KD AS')
    assert result == 'Straight'
    
def test_poker_flush():
    result = get_poker_data('4H 8H 2H 9H 7H')
    assert result == 'Flush'
    
def test_poker_straight_flush():
    result = get_poker_data('AC 2C 3C 4C 5C')
    assert result == 'Straight Flush'
    
def test_poker_royal_flush():
    result = get_poker_data('10S JS QS KS AS')
    assert result == 'Royal Flush'