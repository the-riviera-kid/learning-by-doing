from min_length_requirement import MustMeetMinimumLengthRequirement

def test_min_length_requirement():
    assert MustMeetMinimumLengthRequirement()

def test_password_meets_min_length():
    password = MustMeetMinimumLengthRequirement()
    assert password.check('Hello') == True

def test_password_under_min_length():
    password = MustMeetMinimumLengthRequirement()
    assert password.check('Hi') == False

def test_message():
    password = MustMeetMinimumLengthRequirement()
    assert password.message() == 'The password must be at least 5 characters.'