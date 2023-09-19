from word_collection import WordCollection
from hangman import Hangman
from guess_counter import GuessCounter

class GameManager:
    def __init__(self, word_list: WordCollection) -> None:
        self.word_list = word_list
        self.word = self.word_list.get_random_word()

    def play(self) -> object:
        guesses = GuessCounter()
        while self.word.has_blanks and guesses.current_guesses != 0:
            good_guess = self.word.is_letter_in_word(input('Guess a letter: '))
            if not good_guess:
                guesses_remaining = guesses.update_guesses()
                hangman = Hangman(guesses_remaining)
                print(hangman, end='\n\n')
                print(guesses, end='\n\n')
            print(self.word.current_word, end='\n\n')
        return self.word


if __name__ == '__main__':
    words = ['cat', 'dog']
    word_list = WordCollection(words)
    play = GameManager(word_list)
    play.play()