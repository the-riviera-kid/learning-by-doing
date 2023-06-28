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

def test_high_card():
    hand = PokerHand('AS 10S 5H 7C 6S').get_hand_name()
    assert hand == 'High Card'

def test_high_card():
    hand = PokerHand('AS 10S 5H 10C 6S').get_hand_name()
    assert hand == 'One Pair'