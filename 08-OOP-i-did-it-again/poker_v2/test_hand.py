from hand import Hand
import pytest
from typing import Any

def check_type_errors(user_input: Any) -> None:
    with pytest.raises(TypeError):
        Hand(user_input)

def test_invalid_hand_none() -> None:
    check_type_errors(None)

def test_invalid_hand_int() -> None:
    check_type_errors(2348976)

def test_invalid_hand_list() -> None:
    check_type_errors([])

def check_value_errors(user_input: str) -> None:
    with pytest.raises(ValueError):
        Hand(user_input)
    
def test_invalid_hand_empty_string() -> None:
    check_value_errors('')
    
def test_invalid_hand_3_cards() -> None:
    check_value_errors('3D 4H 8C')

def test_invalid_hand_6_cards() -> None:
    check_value_errors('3D 4H 8C JD KS AH')

def test_duplicate_card() -> None:
    check_value_errors('JC JD JS JC 5H')

def test_valid_hand() -> None:
    hand = Hand('3D 4H 8C JD KS')
    assert hand.hand == ['3D', '4H', '8C', 'JD', 'KS']

def compare_hand_to_name(hand: str, poker_name: tuple[str, int]) -> None:
    assert Hand(hand)._check_poker_hand() == poker_name

def test_high_card() -> None:
    compare_hand_to_name('AS 10S 5H 7C 6S', ('High Card', 1))

def test_one_pair() -> None:
    compare_hand_to_name('AS 10S 5H 10C 6S', ('One Pair', 2))

def test_two_pair() -> None:
    compare_hand_to_name('3H 8C 8H 9S 3D', ('Two Pair', 3))

def test_three_of_a_kind() -> None:
    compare_hand_to_name('6S 6H 7C JD 6D', ('Three Of A Kind', 4))

def test_four_of_a_kind() -> None:
    compare_hand_to_name('JC JD JS JH 5H', ('Four Of A Kind', 8))

def test_straight_v1() -> None:
    compare_hand_to_name('2H 3C 4S 5H 6D', ('Straight', 5))

def test_straight_varied_order() -> None:
    compare_hand_to_name('JD 8C 10S 9S 7D', ('Straight', 5))

def test_straight_ace_low() -> None:
    compare_hand_to_name('AS 2H 3C 4S 5D', ('Straight', 5))

def test_straight_ace_high() -> None:
    compare_hand_to_name('10H JH QC KD AS', ('Straight', 5))

def test_flush() -> None:
    compare_hand_to_name('4H 8H 2H 9H 7H', ('Flush', 6))

def test_straight_flush() -> None:
    compare_hand_to_name('AC 2C 3C 4C 5C', ('Straight Flush', 9))

def test_royal_flush() -> None:
    compare_hand_to_name('10S JS QS KS AS', ('Royal Flush', 10))

def test_full_house() -> None:
    compare_hand_to_name('4H 4D 4C 8S 8D', ('Full House', 7))

def test_royal_flush_greater_than_straight_flush() -> None:
    assert Hand('10S JS QS KS AS').placement > Hand('AC 2C 3C 4C 5C').placement

def test_four_of_a_kind_than_straight_flush() -> None:
    assert Hand('JC JD JS JH 5H').placement > Hand('6S 6H 7C JD 6D').placement

def test_four_of_a_kind_tie() -> None:
    assert Hand('JC JD JS JH 5H').placement == Hand('JC JD JS JH 5H').placement

# def test_four_of_a_kind_tie_different_hands() -> None:
#     assert Hand('JC JD JS JH 5H') > Hand('9C 9D 9S 9H 6H')