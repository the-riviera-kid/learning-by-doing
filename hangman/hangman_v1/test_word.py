from word import Word


def test_word() -> None:
    assert Word('a')

def test_generate_word() -> None:
    word = Word('a')
    assert word._generate_word() == 'cat'

def test_guessed_letter_in_word() -> None:
    word = Word('a')
    word._generate_word()
    word.check_guess_in_word()
    assert word.display_blanks_or_letters() == '_ a _'

def test_display_blanks() -> None:
    word = Word('t')
    word._generate_word()
    word.check_guess_in_word()
    assert word.display_blanks_or_letters() == '_ _ t'