from password_checker import PasswordChecker
from requirements import MustContainCapitalRequirement, MustContainNumberRequirement, MustMeetMinimumLengthRequirement

def main():
    checker = PasswordChecker([
        MustContainCapitalRequirement(),
        MustContainNumberRequirement(),
        MustMeetMinimumLengthRequirement(6)
    ])
    password = input('Please enter new password: ')
    if not checker.check(password):
        for message in checker.messages():
            print(message)


if __name__ == '__main__':
    main()
