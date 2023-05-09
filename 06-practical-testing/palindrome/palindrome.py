from pure_palindrome import check_if_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome


def main():
    user_input = input('Type your palindrome: ')
    is_invalid = check_if_invalid(user_input)
    if is_invalid is not None:
        print(is_invalid)
    
    cleaned_input = clean_user_input(user_input)
    
    palindrome = check_for_palindrome(cleaned_input)
    print(palindrome)

if __name__ == '__main__':
    main()