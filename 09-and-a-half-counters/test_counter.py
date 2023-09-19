from counter import Counter

def test_counter_adds_1() -> None:
    result = Counter()
    assert result.add() == 1

def test_counter_adds_again() -> None:
    result = Counter()
    result.add()
    assert result.add() == 2

def test_counter_total() -> None:
    result = Counter()
    result.add()
    result.add()
    result.add()
    assert result.total() == 3

def test_counter_totals() -> None:
    result_1 = Counter()
    result_2 = Counter()
    result_1.add()
    result_2.add()
    result_1.add()
    assert result_1.total() == 2
    assert result_2.total() == 1

def test_counter_reset() -> None:
    result_1 = Counter()
    result_2 = Counter()
    result_1.add()
    result_2.add()
    result_1.add()
    assert result_1.total() == 2
    assert result_2.total() == 1
    assert result_1.reset() == 0
    assert result_2.total() == 1
