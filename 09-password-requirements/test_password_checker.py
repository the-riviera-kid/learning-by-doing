from password_checker import PasswordChecker
from number_requirement import MustContainNumberRequirement
from capital_requirement import MustContainCapitalRequirement
from min_length_requirement import MustMeetMinimumLengthRequirement
import pytest

@pytest.mark.parametrize('input_password, requirements, expected_check, expected_messages', [
    ('8', [MustContainNumberRequirement()], True, []),
    ('Hi123', [MustContainNumberRequirement(), MustContainCapitalRequirement()], True, []),
    ('hi123', [MustContainNumberRequirement(), MustContainCapitalRequirement()], False, ['The password must contain at least one capital letter.']),
    ('sausage', [MustContainNumberRequirement()], False, ['The password must contain at least one number.']),
    ('sausage', [MustContainNumberRequirement(), MustContainCapitalRequirement()], False, ['The password must contain at least one number.', 'The password must contain at least one capital letter.']),
    ('hello123', [MustMeetMinimumLengthRequirement()], True, []),
    ('8', [MustMeetMinimumLengthRequirement()], False, ['The password must be at least 5 characters.']),
    ('Hi123', [MustMeetMinimumLengthRequirement(), MustContainCapitalRequirement()], True, []),
    ('Hello', [MustMeetMinimumLengthRequirement(), MustContainCapitalRequirement()], True, []),
    ('hi', [MustMeetMinimumLengthRequirement(), MustContainCapitalRequirement(), MustContainNumberRequirement()], False, ['The password must be at least 5 characters.', 'The password must contain at least one capital letter.', 'The password must contain at least one number.']),
])

def test_requirements(input_password, requirements, expected_check, expected_messages):
    password = PasswordChecker(requirements)
    assert password.check(input_password) == expected_check
    assert password.message() == expected_messages
