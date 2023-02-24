'''
    Challenge:
    The computer picks a word from a selection it knows, shows you the blanks,
    and asks you to guess. Every successful guess fills in those blanks.
    Every failed guess draws a new piece of the hangman. You have six chances to win.

    Problem Steps:
    1. Computer picks a random word from a selection
    2. Give the player the rules to play the game (including that they have 6 chances to guess)
    3. Show player the blanks for each letter of the chosen word
    4. Ask the player to guess a letter
    5. Check if the guessed letter is in the word
    6. If it is, fill in those blanks
    7. Repeat from step 4
    8. If no match, draw a piece of the hangman (decreasing the count by 1)
    9. Repeat from step 4
    10. If all the letters are filled, player wins
    11. Check if player wants to play again - Print 'Would you like to play again? y/n '
    12. If 'y' return to step 1 and set number of guesses back to 6
    13. If 'n' exit()
    14. When guesses == 0, hangman is complete - print 'Too bad, you've run out of guesses'
    15. Return to step 11
'''

import random


def main():
    count = 6
    correct_guesses = []
    word = target_word()
    print(word)
    print_blanks(word)
    
    while blanks(word, correct_guesses) and count > 0:
        guess = play_game(word, correct_guesses)
        if guess not in word:
            count -=1
            hangman(count)


def target_word():
    word_list = ['asleep', 'artist', 'beauty', 'agreed', 'doubts', 'stones', 'emerge', 'legend', 'finish', 'clever', 'island']
    word = random.choice(word_list)
    return word


def print_blanks(word):
    for letter in word:
        print('_', end=' ')
    print('\n\n')


def blanks(word, correct_guesses):
    for letter in word:
        if letter not in correct_guesses:
            return True
    return False
    

def play_game(word, correct_guesses):
    guess = user_guess()
    compare_guess_to_word(word, guess, correct_guesses)
    return guess


def user_guess():
    guess = input('Guess your letter: ')
    return guess


def compare_guess_to_word(word, guess, correct_guesses):
    for letter in word:
        if letter == guess or letter in correct_guesses:
            print(letter, end=' ')
            correct_guesses.append(guess)
        else:
            print('_', end=' ')
    print('\n\n')


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