from typing import List


class PasswordChecker:
    def __init__(self, requirements) -> None:
        self.requirements = requirements
        self.recent_messages: List[str] = []

    def check(self, password):
        self.recent_messages = [r.message() for r in self.requirements if not r.check(password)]
        return all([r.check(password) for r in self.requirements])
        
    def message(self):
        return self.recent_messages
