from password_checker import PasswordChecker
from requirements import MustContainCapitalRequirement, MustContainNumberRequirement, MustMeetMinimumLengthRequirement

def test_create_checker():
    assert PasswordChecker([])

def test_checker_no_requirements():
    checker = PasswordChecker([])
    assert checker.check('')
    assert checker.messages() == []

def test_checker_two_requirements():
    checker = PasswordChecker([MustContainCapitalRequirement(), MustContainNumberRequirement()])
    assert not checker.check('poo')
    assert 'Password must contain at least one capital letter.' in checker.messages()
    assert 'Password must contain at least one number.' in checker.messages()
    assert len(checker.messages()) == 2

