def check_if_invalid(user_input):
    if user_input == '' or not isinstance(user_input, str):
        return 'Sorry, that is invalid input'


def clean_user_input(user_input):
    user_input_list = [i for i in user_input if i.isalnum()]
    user_input = ''.join(user_input_list)
    return user_input.lower()


def check_for_palindrome(user_input):
    if user_input[:] != user_input[::-1]:
        return 'Not a palindrome'
    return 'Is palindrome'