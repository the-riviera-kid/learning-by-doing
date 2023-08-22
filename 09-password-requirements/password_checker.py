class PasswordChecker:
    def __init__(self, requirements):
        self.requirements = requirements
        self.problems = []

    def check(self, password):
        problems = [x.message() for x in self.requirements if not x.check(password)]
        self.problems = problems
        return not any(problems)

    def messages(self):
        return self.problems

