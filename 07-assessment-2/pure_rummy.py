def rummy(user_input):
    is_valid = check_valid(user_input)
    return is_valid


def check_valid(user_input):
    if user_input is None or user_input == '' or not isinstance(user_input, str):
        return 'Sorry, that is invalid'