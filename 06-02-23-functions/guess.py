import random

def main():
    target_number = random.randrange(1, 100)
    for remaining_guesses in range(6, 0, -1):
        play(target_number, remaining_guesses)
    end_game_sad(target_number)

def play(target, remaining_guesses):
    has_won = play_round(target, remaining_guesses)
    if has_won:
        end_game_happy(remaining_guesses)

def play_round(target, remaining_guesses):
    print(f'You have {remaining_guesses} guesses remaining.')
    player_guess = get_player_guess()
    return check_guess(player_guess, target)

def get_player_guess():
    guess = input('What do you guess? : ')
    return int(guess)

def check_guess(guess, target):
    if guess == target:
        return True
    else:
        print_higher_or_lower(guess, target)
        return False

def print_higher_or_lower(guess, target):
    if guess > target:
        print('You guessed too high!')
    else:
        print('You guessed too low!')

def end_game_happy(remaining_guesses):
    print(f'Well done! You had {remaining_guesses} remaining.')
    exit(0)

def end_game_sad(answer):
    print(f'Sorry! The answer was {answer}')






if __name__ == '__main__':
    main()
