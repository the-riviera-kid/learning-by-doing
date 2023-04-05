import pytest
from blanking import blank

def test_blank():
    with pytest.raises(TypeError, match='hangman'):
        blank(None, None)

def test_blank_valid_word_no_characters():
    result = blank('asparagus', None)
    assert result == '_________'

def test_blank_no_word_valid_characters():
    result = blank('asparagus', 'a')
    assert result == 'a__a_a___'

def test_blank_work_complete():
    result = blank('asparagus', 'asprgu')
    assert result == 'asparagus'

def test_blank_characters_not_in_word():
    result = blank('coffee', 'fsa')
    assert result == '__ff__'

def test_blank_two_guessed_correctly():
    result = blank('cabbage', 'xbog')
    assert result == '__bb_g_'

def test_blank_same_char_guessed_multiple_times():
    result = blank('broccoli', 'leql')
    assert result == '______l_'

def test_blank_word_is_wrong_type():
    with pytest.raises(TypeError, match='hangman'):
        blank(23, 'ohdear')