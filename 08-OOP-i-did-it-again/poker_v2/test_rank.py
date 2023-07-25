from rank import Rank
import pytest

def test_rank_exits():
    assert Rank

def check_type_errors(user_input):
    with pytest.raises(TypeError):
        Rank(user_input)

def test_invalid_rank_none():
    check_type_errors(None)

def test_invalid_rank_int():
    check_type_errors(3)

def test_invalid_rank_list():
    check_type_errors([])

def test_invalid_rank_dict():
    check_type_errors({})

def check_value_errors(user_input):
    with pytest.raises(ValueError):
        Rank(user_input)
    
def test_invalid_rank_empty_string():
    check_value_errors('')

def test_invalid_rank_f():
    check_value_errors('1')

def test_valid_rank():
    rank = Rank('6')
    assert rank.rank == '6'

def test_valid_rank_J():
    rank = Rank('J')
    assert rank.rank == 'J'

def test_compare_ranks():
    assert Rank('Q') == Rank('Q')

def test_rank_greater_than_other():
    assert Rank('K') > Rank('Q')

def test_rank_greater_than_other_with_10():
    assert Rank('10') > Rank('9')

def test_rank_greater_than_other_with_ace():
    assert Rank('A') > Rank('K')

def test_rank_less_than_other():
    assert Rank('8') < Rank('9')

def test_subtract_ranks():
    assert Rank('Q') - Rank('J') == 1
