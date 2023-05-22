from pure_rummy import rummy


def main():
    user_input = input('What is your hand? ')
    message = rummy(user_input)
    return message

if __name__ == '__main__':
    main()