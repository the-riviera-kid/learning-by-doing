from poker_hand import PokerHand
import pytest

def test_PokerHand_exists():
    assert PokerHand('2H 4D 6S 10C 3C')

def test_invalid_hand_None():
    with pytest.raises(TypeError):
        PokerHand(None)

def test_invalid_hand_int():
    with pytest.raises(TypeError):
        PokerHand(2)

def test_invalid_hand_empty_string():
    with pytest.raises(TypeError):
        PokerHand('')

def test_invalid_hand_too_short():
    with pytest.raises(TypeError):
        PokerHand('2H 4D 6S 10C')

def test_invalid_hand_too_long():
    with pytest.raises(TypeError):
        PokerHand('2H 4D 6S 10C 6S 10C')

def test_invalid_cards():
    with pytest.raises(TypeError):
        PokerHand('2H 4D 6S 10C 6Z')

def test_invalid_reject_duplicate_cards():
    with pytest.raises(TypeError):
        PokerHand('JC JD JS JC 5H')

def test_high_card():
    hand = PokerHand('AS 10S 5H 7C 6S').get_hand_name()
    assert hand == 'High Card'

def test_one_pair():
    hand = PokerHand('AS 10S 5H 10C 6S').get_hand_name()
    assert hand == 'One Pair'

def test_two_pair():
    hand = PokerHand('3H 8C 8H 9S 3D').get_hand_name()
    assert hand == 'Two Pair'

def test_three_of_a_kind():
    hand = PokerHand('6S 6H 7C JD 6D').get_hand_name()
    assert hand == 'Three Of A Kind'

def test_four_of_a_kind():
    hand = PokerHand('JC JD JS JH 5H').get_hand_name()
    assert hand == 'Four Of A Kind'

def test_full_house():
    hand = PokerHand('4H 4D 4C 8S 8D').get_hand_name()
    assert hand == 'Full House'

def test_straight():
    hand = PokerHand('2H 3C 4S 5H 6D').get_hand_name()
    assert hand == 'Straight'

def test_straight_4_cards():
    hand = PokerHand('2H 3C 4S 5H 5C').get_hand_name()
    assert hand == 'One Pair'

'''
Straight
All five cards form a continuous sequence
"2H 3C 4S 5H 6D", or "JD 8C 10S 9S 7D"
An Ace can be low ("AS 2H 3C 4S 5D") or high ("10H JH QC KD AS")
but not both at the same time.
'''