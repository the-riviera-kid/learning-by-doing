'''
    Challenge:
    The classic number guessing game.
    The computer picks a number between 1 and 100, and asks you to guess.
    It tells you if you were too high or too low, and gives you six chances to guess.

    Problem Steps:
    1. Computer gets a random number between 1 and 100
    2. Give the user the rules to play the game (including that they have 6 chances to guess)
    3. Print - You have {number} guesses
    4. Ask user to guess a number between 1 and 100
    5. Decrease the guesses count by 1
    6. Check if the guessed number is correct
    7. If correct, user wins - print 'You guessed correctly!'
    8. Check if user wants to play again - Print 'Would you like to play again? y/n '
    9. If 'y' return to step 1 and set number of guesses back to 6
    10. If 'n' exit()
    11. If the number is too high - print 'Your guess is too high'
    12. Return to step 2
    13. If the number is too low - print 'Your guess is too low'
    14. Return to step 2
    15. When guesses == 0, print 'Too bad, you've run out of guesses'
    16. Return to step 7
'''

from random import randint


def main():
    game_rules()
    guesses = 6
    user_wins = False
    random_number = get_random_number()
    while not user_wins and guesses != 0:
        guesses -= 1
        user_wins = play_game(random_number, guesses)


def play_game(random_number, guesses):
    user_number = get_user_number()
    too_high = number_too_high(user_number, random_number)
    too_low = number_too_low(user_number, random_number)
    incorrect_guess_countdown(too_high, too_low, guesses)
    user_wins = check_user_wins(user_number, random_number)
    return user_wins


def game_rules():
    print()
    print("This is a number guessing game. \nYou have 6 chances to guess the number correctly. \nLet's play!")
    print()
    print(f'You have 6 guesses.')


def get_random_number():
    number = randint(1, 101)
    return number


def get_user_number():
    print()
    guess = int(input('Guess a number between 1 and 100: '))
    print()
    return guess


def number_too_high(user_guess, target_number):
    if user_guess > target_number:
        print('Your guess is too high')
        return True


def number_too_low(user_guess, generated_number):
    if user_guess < generated_number:
        print('Your guess is too low')
        return True


def incorrect_guess_countdown(too_high, too_low, guesses_remaining):
    if too_high or too_low:
        print(f'You have {guesses_remaining} guesses remaining')
        if guesses_remaining == 0:
            print(f'Better luck next time!')
            print()
        return True


def check_user_wins(user_guess, generated_number):
    if user_guess == generated_number:
        print('Congratulations, you guessed the correct number!')
        print()
        return replay()
    else:
        return False


def replay():
    play_again = input('Would you like to play again? (y/n) ')
    if play_again == 'y':
        print()
        main()
    else:
        print()
        exit()


if __name__ == '__main__':
    main()
