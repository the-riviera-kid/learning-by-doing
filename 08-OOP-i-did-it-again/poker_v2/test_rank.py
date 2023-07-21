from rank import Rank
import pytest

def test_rank_exits():
    assert Rank

def test_invalid_rank_none():
    with pytest.raises(TypeError):
        Rank(None)

def test_invalid_rank_int():
    with pytest.raises(TypeError):
        Rank(3)

def test_invalid_rank_list():
    with pytest.raises(TypeError):
        Rank([])

def test_invalid_rank_dict():
    with pytest.raises(TypeError):
        Rank({})

def test_invalid_rank_empty_string():
    with pytest.raises(ValueError):
        Rank('')

def test_invalid_rank_f():
    with pytest.raises(ValueError):
        Rank('1')

def test_valid_suit():
    rank = Rank('6')
    assert rank.rank == '6'

def test_valid_rank_J():
    rank = Rank('J')
    assert rank.rank == 'J'

def test_compare_ranks():
    assert Rank('Q') == Rank('Q')

def test_rank_greater_than_other():
    assert Rank('K') > Rank('Q')

def test_rank_less_than_other():
    assert Rank('8') < Rank('9')
