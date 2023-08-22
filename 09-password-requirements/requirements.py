class MustMeetMinimumLengthRequirement:
    def __init__(self, min_len):
        self.min_len = min_len

    def check(self, password):
        return len(password) >= self.min_len

    def message(self):
        return f'Password must be at least {self.min_len} characters long.'

class MustContainCapitalRequirement:
    def check(self, password):
        return any(x.isupper() for x in password)

    def message(self):
        return 'Password must contain at least one capital letter.'

class MustContainNumberRequirement:
    def check(self, password):
        return any(x.isdigit() for x in password)

    def message(self):
        return 'Password must contain at least one number.'

