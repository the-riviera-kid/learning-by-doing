from capital_requirement import MustContainCapitalRequirement

def test_capital_requirement():
    assert MustContainCapitalRequirement()

def test_password_contains_a_capital_letter():
    password = MustContainCapitalRequirement()
    result = password.check('Hello')
    assert result == True

def test_password_contains_no_capital_letter():
    password = MustContainCapitalRequirement()
    result = password.check('hello')
    assert result == False

def test_message():
    password = MustContainCapitalRequirement()
    result = password.message()
    assert result == 'The password must contain at least one capital letter.'