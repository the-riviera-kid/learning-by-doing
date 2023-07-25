from hand import Hand
import pytest

def test_hand_exists():
    assert Hand

def check_type_errors(user_input):
    with pytest.raises(TypeError):
        Hand(user_input)

def test_invalid_hand_none():
    check_type_errors(None)

def test_invalid_hand_int():
    check_type_errors(2348976)

def test_invalid_hand_list():
    check_type_errors([])

def check_value_errors(user_input):
    with pytest.raises(ValueError):
        Hand(user_input)
    
def test_invalid_hand_empty_string():
    check_value_errors('')
    
def test_invalid_hand_3_cards():
    check_value_errors('3D 4H 8C')

def test_invalid_hand_6_cards():
    check_value_errors('3D 4H 8C JD KS AH')

def test_duplicate_card():
    check_value_errors('JC JD JS JC 5H')

def test_valid_hand():
    hand = Hand('3D 4H 8C JD KS')
    assert hand.hand == ['3D', '4H', '8C', 'JD', 'KS']

def compare_hand_to_name(hand, poker_name):
    assert Hand(hand)._check_poker_hand() == poker_name

def test_high_card():
    compare_hand_to_name('AS 10S 5H 7C 6S', 'High Card')

def test_one_pair():
    compare_hand_to_name('AS 10S 5H 10C 6S', 'One Pair')

def test_two_pair():
    compare_hand_to_name('3H 8C 8H 9S 3D', 'Two Pair')

def test_three_of_a_kind():
    compare_hand_to_name('6S 6H 7C JD 6D', 'Three Of A Kind')

def test_four_of_a_kind():
    compare_hand_to_name('JC JD JS JH 5H', 'Four Of A Kind')

# def test_straight():
#     compare_hand_to_name('2H 3C 4S 5H 6D', 'Straight')
