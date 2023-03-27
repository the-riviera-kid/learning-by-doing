import random


def main():
    # Setup
    guesses_remaining = 6
    word_list = ['asleep', 'artist', 'beauty', 'agreed', 'doubts', 'stones', 'emerge', 'legend', 'finish', 'clever', 'island']
    word = random.choice(word_list)
    print(word)
    correct_guesses = []
    print_blanks(word)

    while blanks_are_left(word, correct_guesses) and guesses_remaining > 0:
        user_letter = play_game(word, correct_guesses)
        if user_letter not in word:
            guesses_remaining -= 1
            hangman(guesses_remaining)


def blanks_are_left(word, correct_guesses):
    for letter in word:
        if letter not in correct_guesses:
            return True
    return False


def print_blanks(word):
    for letter in word:
        print('_', end=' ')
    print()


def play_game(word, correct_guesses):
    user_letter = get_user_guess()
    print_result(word, user_letter, correct_guesses)
    return user_letter


def get_user_guess():
    user_letter = input('Enter your letter: ')
    return user_letter


def print_result(word, user_letter, correct_guesses):
    for letter in word:
        if user_letter == letter or letter in correct_guesses:
            print(letter, end=' ')
            correct_guesses.append(user_letter)
        else:
            print('_', end=' ')
    print()


def hangman(guesses_remaining):
    if guesses_remaining == 5:
        print_hangman = get_hangman_five_chances()
    elif guesses_remaining == 4:
        print_hangman = get_hangman_four_chances()
    elif guesses_remaining == 3:
        print_hangman = get_hangman_three_chances()
    elif guesses_remaining == 2:
        print_hangman = get_hangman_two_chances()
    elif guesses_remaining == 1:
        print_hangman = get_hangman_one_chance()
    else:
        print_hangman = get_hangman_zero_chances()
    
    for line in print_hangman:
        print(line)


def get_hangman_five_chances():
    return [
        "_________",
        "|      |",
        "|      O",
        "|",
        "|",
        "|",
        "|________"
    ]


def get_hangman_four_chances():
    return [
        "_________",
        "|      |",
        "|      O",
        "|      |",
        "|      |",
        "|",
        "|________"
    ]


def get_hangman_three_chances():
    return [
        "_________",
        "|      |",
        "|      O",
        "|     \|",
        "|      |",
        "|",
        "|________"
    ]


def get_hangman_two_chances():
    return [
        "_________",
        "|      |",
        "|      O",
        "|     \|/",
        "|      |",
        "|",
        "|________"
    ]


def get_hangman_one_chance():
    return [
        "_________",
        "|      |",
        "|      O",
        "|     \|/",
        "|      |",
        "|     /  ",
        "|________"
    ]


def get_hangman_zero_chances():
    return [
        "_________",
        "|      |",
        "|      O",
        "|     \|/",
        "|      |",
        "|     / \ ",
        "|________"
    ]



if __name__ == '__main__':
    main()