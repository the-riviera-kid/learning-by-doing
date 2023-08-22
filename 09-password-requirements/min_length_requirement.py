class MustMeetMinimumLengthRequirement:
    def __init__(self):
        self.min_length = 5

    def check(self, password):
        return len(password) >= self.min_length
    
    def message(self):
        return f'The password must be at least {self.min_length} characters.'
        