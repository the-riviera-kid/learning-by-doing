from password_checker import PasswordChecker
from number_requirement import MustContainNumberRequirement
from capital_requirement import MustContainCapitalRequirement
from min_length_requirement import MustMeetMinimumLengthRequirement

PASSWORD_CHECKER = PasswordChecker([MustContainNumberRequirement()])

def test_password_checker():
    assert PASSWORD_CHECKER

# def compare_check_input_with_expected_output(password, output): # check()
#     result = PASSWORD_CHECKER.check(password)
#     assert result == output

# def compare_message_input_with_expected_output(password, output): # message()
#     PASSWORD_CHECKER.check(password)
#     result = PASSWORD_CHECKER.message()
#     assert result == output

def compare_check_message_input_with_expected_output(password, check_output, msg_output): # message()
    check = PASSWORD_CHECKER.check(password)
    message = PASSWORD_CHECKER.message()
    assert check == check_output
    assert message == msg_output

def test_meets_number_requirements():
    compare_check_message_input_with_expected_output('8', True, [])

def test_does_not_meet_number_requirements():
    compare_check_message_input_with_expected_output('sausage', False, ['The password must contain at least one number.'])

# def test_meets_number_requirements():
#     compare_check_input_with_expected_output('8', True) # check, meets
#     compare_message_input_with_expected_output('8', []) # message, meets

# def test_check_meets_number_requirements(): # check, meets
#     password = PasswordChecker([MustContainNumberRequirement()])
#     assert password.check('8') == True

# def test_message_meets_number_requirements(): # message, meets
#     password = PasswordChecker([MustContainNumberRequirement()])
#     password.check('8')
#     assert password.message() == []

# def test_does_not_meet_number_requirements():
#     compare_check_input_with_expected_output('sausage', False) # check, does not meet
#     compare_message_input_with_expected_output('sausage', ['The password must contain at least one number.']) # message, does not meet

# def test_check_does_not_meet_number_requirements(): # check, does not meet
#     password = PasswordChecker([MustContainNumberRequirement()])
#     assert password.check('sausage') == False

# def test_message_does_not_meet_number_requirements(): # message, does not meet
#     password = PasswordChecker([MustContainNumberRequirement()])
#     password.check('sausage')
#     assert password.message() == ['The password must contain at least one number.']

def test_message_does_not_meet_number_requirements_no_call_to_check_method(): # no call to check()
    password = PasswordChecker([MustContainNumberRequirement()])
    assert password.message() == []

# =============================================================================================

def test_message_meets_capital_requirements(): # message, meets
    password = PasswordChecker([MustContainCapitalRequirement()])
    password.check('Hi')
    assert password.message() == []

def test_message_does_not_meet_capital_requirements(): # message, does not meet
    password = PasswordChecker([MustContainCapitalRequirement()])
    password.check('hi')
    assert password.message() == ['The password must contain at least one capital letter.']

# =============================================================================================

def test_check_meets_min_length_requirements(): # check, meets
    password = PasswordChecker([MustMeetMinimumLengthRequirement()])
    assert password.check('hello123') == True

def test_check_does_not_meet_min_length_requirements(): # check, does not meet
    password = PasswordChecker([MustMeetMinimumLengthRequirement()])
    assert password.check('8') == False

def test_message_meets_min_length_requirements(): # message, meets
    password = PasswordChecker([MustMeetMinimumLengthRequirement()])
    password.check('hello123')
    assert password.message() == []

def test_message_does_not_meet_min_length_requirements(): # message, does not meet
    password = PasswordChecker([MustMeetMinimumLengthRequirement()])
    password.check('8')
    assert password.message() == ['The password must be at least 5 characters.']

# =============================================================================================

def test_check_meets_number_and_capital_requirements(): # check, meets all
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('Hi123') == True

def test_message_meets_number_and_capital_requirements(): # message, meets all
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    password.check('Hi123')
    assert password.message() == []

def test_check_meets_capital_but_not_number_requirement(): # check, meets capital, not number
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('Hello') == False
    
def test_check_meets_number_but_not_capital_requirement(): # check, meets number, not capital
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('hello123') == False

def test_message_meets_capital_but_not_number_requirement(): # message, meets capital, not number
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    password.check('Hello')
    assert password.message() == ['The password must contain at least one number.']

def test_message_meets_number_but_not_capital_requirement(): # message, meets number, not capital
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    password.check('8')
    assert password.message() == ['The password must contain at least one capital letter.']

def test_message_does_not_meet_number_or_capital_requirement(): # message, does not meet any
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    password.check('hello')
    assert password.message() == ['The password must contain at least one number.', 'The password must contain at least one capital letter.']

def test_check_meets_number_capital_min_length_requirements(): # check, meets all
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement(), MustMeetMinimumLengthRequirement()])
    assert password.check('Hello123') == True

def test_message_meets_number_capital_min_length_requirements(): # message, meets all
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement(), MustMeetMinimumLengthRequirement()])
    password.check('Hello123')
    assert password.message() == []

def test_check_meets_capital_but_not_number_or_min_length_requirement(): # check, meets capital, not number or min len
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('Hello') == False
    
def test_check_meets_number_but_not_capital_or_min_length_requirement(): # check, meets number, not capital or min len
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('hi123') == False

def test_check_meets_min_length_but_not_number_or_capital_requirement(): # check, meets min len, not number or capital
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('helloooo') == False
    
def test_check_meets_min_len_and_number_but_not_capital_requirement(): # check, meets min len and number, not capital
    password = PasswordChecker([MustContainNumberRequirement(), MustContainCapitalRequirement()])
    assert password.check('hello123') == False
