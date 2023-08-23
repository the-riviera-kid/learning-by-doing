from capital_requirement import MustContainCapitalRequirement

def test_capital_requirement():
    assert MustContainCapitalRequirement()

def test_password_contains_a_capital_letter():
    password = MustContainCapitalRequirement()
    assert password.check('Hello') == True

def test_password_contains_no_capital_letter():
    password = MustContainCapitalRequirement()
    assert password.check('hello') == False

def test_message():
    password = MustContainCapitalRequirement()
    assert password.message() == 'The password must contain at least one capital letter.'