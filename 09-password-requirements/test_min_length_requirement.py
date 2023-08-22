from min_length_requirement import MustMeetMinimumLengthRequirement

def test_min_length_requirement():
    assert MustMeetMinimumLengthRequirement()

def test_password_meets_min_length():
    password = MustMeetMinimumLengthRequirement()
    result = password.check('Hello')
    assert result == True

def test_password_under_min_length():
    password = MustMeetMinimumLengthRequirement()
    result = password.check('Hi')
    assert result == False

def test_message():
    password = MustMeetMinimumLengthRequirement()
    result = password.message()
    assert result == 'The password must be at least 5 characters.'