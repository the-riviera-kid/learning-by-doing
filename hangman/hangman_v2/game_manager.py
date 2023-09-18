from word_collection import WordCollection
from hangman import Hangman

class GameManager:
    def __init__(self, word_list: WordCollection) -> None:
        self.word_list = word_list
        self.word = self.word_list.get_random_word()

    def play(self) -> object:
        guesses = 6
        while self.word.has_blanks and guesses != 0:
            good_guess = self.word.is_letter_in_word(input('Guess a letter: '))
            if not good_guess:
                guesses -= 1
                hangman = Hangman(guesses)
                print(hangman)
                print(f'You have {guesses} guesses')
            print(self.word.current_word)
        if guesses == 0:
            print(f'Game Over')
        return self.word


if __name__ == '__main__':
    words = ['cat', 'dog']
    word_list = WordCollection(words)
    play = GameManager(word_list)
    play.play()