from requirements import (
    MustMeetMinimumLengthRequirement,
    MustContainCapitalRequirement,
    MustContainNumberRequirement
)

def test_minimum_length():
    req = MustMeetMinimumLengthRequirement(8)
    assert req.check('thisisok')
    assert req.check('thisisgud')
    assert not req.check('thisbad')
    assert req.message() == 'Password must be at least 8 characters long.'

def test_contains_capital():
    req = MustContainCapitalRequirement()
    assert req.check('ThisOk')
    assert not req.check('thisbad')
    assert req.message() == 'Password must contain at least one capital letter.'

def test_contains_number():
    req = MustContainNumberRequirement()
    assert req.check('th1s1s0k')
    assert not req.check('thisisok')
    assert req.message() == 'Password must contain at least one number.'
