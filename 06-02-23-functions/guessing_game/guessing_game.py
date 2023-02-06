'''
    Challenge:
    The classic number guessing game.
    The computer picks a number between 1 and 100, and asks you to guess.
    It tells you if you were too high or too low, and gives you six chances to guess.

    Problem Steps:
    1. Computer gets a random number between 1 and 100
    1. Give the user the rules to play the game (including that they have 6 chances to guess)
    2. Print - You have {number} guesses
    3. Ask user to guess a number between 1 and 100
    4. Decrease the guesses count by 1
    5. Check if the guessed number is correct
    6. If correct, user wins - print 'You guessed correctly!'
    7. Check if user wants to play again - Print 'Would you like to play again? y/n '
    8. If 'y' return to step 1 and set number of guesses back to 6
    9. If 'n' exit()
    10. If the number is too high - print 'Your guess is too high'
    11. Return to step 2
    12. If the number is too low - print 'Your guess is too low'
    13. Return to step 2
    14. When guesses == 0, print 'Too bad, you've run out of guesses'
    15. Return to step 7
'''

from random import randint


def computer_number():
    number = randint(1, 100)
    print(number) # For the sake of creation
    return number

def game_rules(number_of_guesses):
    print("This is a number guessing game. \nYou have 6 chances to guess the number correctly. \nLet's play!")
    print()
    print(f'You have {number_of_guesses} guesses.')
    user_guess = int(input('Guess a number between 1 and 100: '))
    return user_guess

def check_user_wins(number, user_guess):
    if user_guess == number:
        print('You guessed correctly!')


def main():
    count = 6
    computer_number()
    game_rules(count)



if __name__ == '__main__':
    main()