from pure_guess_number import get_random_number
from pure_guess_number import get_error_message_or_none
from pure_guess_number import get_game_state


def main():
    target_number = get_random_number()
    invalid = True
    play_game = True
    chances = 6
    while invalid and play_game and chances > 0:
        user_input = input('Guess the number between 1 and 100: ')
        error = get_error_message_or_none(user_input)
        if error:
            print(error)
        else:
            message, play_game = get_game_state(user_input, target_number)
            print(message)
            chances -= 1
            if chances == 0:
                print("You're out of guesses")


if __name__ == '__main__':
    main()
