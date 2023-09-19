from guess_counter import GuessCounter
from word import Word

def test_guess_counter() -> None:
    assert GuessCounter()

def test_remaining_guesses_5() -> None:
    guesses = GuessCounter()
    word = Word('dog')
    word.is_letter_in_word('a')
    assert guesses.update_guesses() == 5