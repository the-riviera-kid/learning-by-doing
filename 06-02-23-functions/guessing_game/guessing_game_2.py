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


def main():
    game_rules()
    random_number = get_random_number()
    user_number = get_user_number()

    too_high = number_too_high(user_number, random_number)
    too_low = number_too_low(user_number, random_number)

    guesses = 6
    incorrect_guess_countdown(too_high, too_low, guesses)
    user_wins = check_user_wins(user_number, random_number)

    while not user_wins and guesses != 0:
        guesses -= 1
        user_number = get_user_number()
        too_high = number_too_high(user_number, random_number)
        too_low = number_too_low(user_number, random_number)
        incorrect_guess_countdown(too_high, too_low, guesses)
        user_wins = check_user_wins(user_number, random_number)


def game_rules():
    print("This is a number guessing game. \nYou have 6 chances to guess the number correctly. \nLet's play!")
    print()
    print(f'You have 6 guesses.')

def get_random_number():
    number = randint(1, 101)
    print(number) # For the sake of creation
    return number

def get_user_number():
    guess = int(input('Guess a number between 1 and 100: '))
    return guess

def number_too_high(user_guess, generated_number):
    if user_guess > generated_number:
        print('Your guess is too high')
        return True

def number_too_low(user_guess, generated_number):
    if user_guess < generated_number:
        print('Your guess is too low')
        return True

def incorrect_guess_countdown(too_high, too_low, guesses_remaining):
    if too_high or too_low:
        print(f'You have {guesses_remaining} guesses remaining')
        return True

def check_user_wins(user_guess, generated_number):
    if user_guess == generated_number:
        print('You guessed correctly!')
        return replay()
    else:
        return False

def replay():
    play_again = input('Would you like to play again? (y/n) ')
    if play_again == 'y':
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
