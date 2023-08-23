from number_requirement import MustContainNumberRequirement

def test_number_requirement():
    assert MustContainNumberRequirement()

def test_password_is_a_number():
    password = MustContainNumberRequirement()
    assert password.check('8') == True

def test_password_is_not_a_number():
    password = MustContainNumberRequirement()
    assert password.check('Hello') == False

def test_password_contains_a_number():
    password = MustContainNumberRequirement()
    assert password.check('Hello123') == True

def test_message():
    password = MustContainNumberRequirement()
    assert password.message() == 'The password must contain at least one number.'