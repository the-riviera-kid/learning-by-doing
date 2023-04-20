'''
    Challenge:
    Write a program which prompts the user for a string representing a poker hand, and displays the name of the hand in response. 
    The names of hands should be printed exactly as they are here (check readme)
    Any invalid input should result in the message "Sorry, that's invalid" and the program stopping.

    Write tests for as much of your program as possible.
    You will have to run your program several times to check it works, but most of your development can and should be done through your tests. 

    poker.py contains import guard and main function.
    poker.py can contain the following statements or functions:
    - print
    - input
    - open

    poker.py cannot contain the following:
    - indexing
    - imports of any modules other than pure_poker
'''

from pure_poker import check_hand_is_invalid
from pure_poker import get_poker_data


def main():
    invalid = True
    while invalid:
        user_hand = input('What is your poker hand? ')
        invalid_hand = check_hand_is_invalid(user_hand)
        if invalid_hand:
            print("Sorry, that's invalid")
        else:
            invalid = False
    poker_hand = get_poker_data(user_hand)
    print(poker_hand)


if __name__ == '__main__':
    main()
