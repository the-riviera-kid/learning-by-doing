class MustContainNumberRequirement:
    def check(self, password):
        return any([p.isnumeric() for p in password])
    
    def message(self):
        return 'The password must contain at least one number.'