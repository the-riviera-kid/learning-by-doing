from number_requirement import MustContainNumberRequirement

def test_number_requirement():
    assert MustContainNumberRequirement()

def test_password_is_a_number():
    password = MustContainNumberRequirement()
    result = password.check('8')
    assert result == True

def test_password_is_not_a_number():
    password = MustContainNumberRequirement()
    result = password.check('Hello')
    assert result == False

def test_password_contains_a_number():
    password = MustContainNumberRequirement()
    result = password.check('Hello123')
    assert result == True

def test_message():
    password = MustContainNumberRequirement()
    result = password.message()
    assert result == 'The password must contain at least one number.'