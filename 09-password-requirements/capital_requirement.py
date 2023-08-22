class MustContainCapitalRequirement:
    def check(self, password):
        return any([p.isupper() for p in password])
    
    def message(self):
        return 'The password must contain at least one capital letter.'
        