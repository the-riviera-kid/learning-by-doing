import random

def main():
    target_number = random.randrange(1, 100)
    lives_left = 6
    results = play(target_number, lives_left)
    end_game(results, target_number)

def play(target, lives_left):
    prompt = printthru(get_prompt(lives_left))
    guess = int(input())
    result = printthru_key(check_guess(guess, target, lives_left), "state")
    return result if result["game_over"] else play(target, lives_left - 1)

def get_prompt(lives_left):
    return f"You have {lives_left} lives left.\nPlease guess a number: "

def check_guess(guess, target, lives_left):
    return {
        "game_over": is_game_over(guess, target, lives_left),
        "state": get_state(guess, target, lives_left),
        "lives_left": lives_left }

def is_game_over(guess, target, lives_left):
    return ( no_lives_left(guess, target, lives_left)
        or guessed_correctly(guess, target, lives_left) )

def get_state(guess, target, lives_left):
    functions = get_state_functions() 
    for func, state in functions:
        if func(guess, target, lives_left):
            return state

def get_state_functions():
    return ((guessed_correctly, "Hooray!"),
            (no_lives_left, "Out of lives"),
            (too_high, "Too high!"),
            (too_low, "Too low!"))

def no_lives_left(guess, target, lives_left):
    return lives_left <= 1

def guessed_correctly(guess, target, lives_left):
    return guess == target

def too_high(guess, target, lives_left):
    return guess > target

def too_low(guess, target, lives_left):
    return guess < target

def end_game(results, correct_answer):
    print("Game Over")
    print(get_string_for_win_state(results, correct_answer))

def get_string_for_win_state(results, correct_answer):
    if results["state"] == "Hooray!":
        return f"You won with {results['lives_left']} lives remaining!"
    else:
        return f"Sorry, but the correct answer was {correct_answer}"

def printthru(s):
    print(s)
    return s

def printthru_key(s, k):
    print(s[k])
    return s

if __name__ == '__main__':
    main()
