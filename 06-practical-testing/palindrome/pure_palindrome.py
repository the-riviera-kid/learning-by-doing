def check_for_invalid(user_input):
    if isinstance(user_input, str):
        for i in user_input:
            if i.isalnum():
                return None
    return 'Sorry, that is invalid input'

def clean_user_input(user_input):
    user_input_list = [i for i in user_input if i.isalnum()]
    user_input_str = "".join(user_input_list)
    return user_input_str.lower()

def check_for_palindrome(user_input):
    if user_input != "".join(reversed(user_input)):
        return 'Not a palindrome'
    return 'Palindrome'


def is_palindrome(user_input):
    invalid = check_for_invalid(user_input)
    if invalid is not None:
        message = invalid

    else:
        cleaned_string = clean_user_input(user_input)        
        palindrome = check_for_palindrome(cleaned_string)
        message = palindrome
    return message