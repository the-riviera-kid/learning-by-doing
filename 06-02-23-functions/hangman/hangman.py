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
    target_word = random_word()
    # set_the_blanks()
    players_guess = get_player_letter()
    match = check_guessed_letter_match(target_word, players_guess)
    chances = count_down(match)
    hangman(chances)


def random_word():
    word_list = ['order', 'carry', 'start', 'agree', 'doubt', 'stone', 'chest', 'ocean', 'eagle', 'cabin', 'island']
    word = random.choice(word_list)
    print(word)
    return word


# def set_the_blanks(word):
#     for letter in word:
#         print('_', end=' ')
#     print()

def get_player_letter():
    guess = input('Guess your letter: ')
    return guess


def check_guessed_letter_match(word, guess):
    for letter in word:
        if guess == letter:
            print('yay')
        else:
            return False


def count_down(match):
    chances_left = 2
    if match == False:
        chances_left -= 1
    return chances_left


def hangman(chances_left):
    if chances_left == 0:
        print_hangman = get_hangman_zero_chances()
    elif chances_left == 1:
        print_hangman = get_hangman_one_chance()

    for line in print_hangman:
        print(line)


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


if __name__ == '__main__':
    main()
