from rank import Rank
import pytest
from typing import Any


def check_type_errors(user_input: Any) -> None:
    with pytest.raises(TypeError):
        Rank(user_input)

def test_invalid_rank_none() -> None:
    check_type_errors(None)

def test_invalid_rank_int() -> None:
    check_type_errors(3)

def test_invalid_rank_list() -> None:
    check_type_errors([])

def test_invalid_rank_dict() -> None:
    check_type_errors({})

def check_value_errors(user_input: str) -> None:
    with pytest.raises(ValueError):
        Rank(user_input)
    
def test_invalid_rank_empty_string() -> None:
    check_value_errors('')

def test_invalid_rank_f() -> None:
    check_value_errors('1')

def test_valid_rank() -> None:
    rank = Rank('6')
    assert rank.rank == '6'

def test_valid_rank_J() -> None:
    rank = Rank('J')
    assert rank.rank == 'J'

def test_compare_ranks() -> None:
    assert Rank('Q') == Rank('Q')

def test_rank_greater_than_other() -> None:
    assert Rank('K') > Rank('Q')

def test_rank_greater_than_other_with_10() -> None:
    assert Rank('10') > Rank('9')

def test_rank_greater_than_other_with_ace() -> None:
    assert Rank('A') > Rank('K')

def test_rank_less_than_other() -> None:
    assert Rank('8') < Rank('9')

def test_subtract_ranks() -> None:
    assert Rank('Q') - Rank('J') == 1
