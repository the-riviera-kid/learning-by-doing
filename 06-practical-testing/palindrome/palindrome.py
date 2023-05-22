from pure_palindrome import is_palindrome

def main():
    user_input = input("Please enter a word: ")
    
    message = is_palindrome(user_input)

    print(message)

if __name__ == '__main__':
    main()