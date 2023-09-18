from word import Word

def test_word() -> None:
    assert Word('cat')

def test_chosen_word() -> None:
    word = 'cat'
    assert word

def test_guessing_letters() -> None:
    word = Word('cat')
    assert word.is_letter_in_word('a')

def test_guessing_letters_false() -> None:
    word = Word('cat')
    assert word.is_letter_in_word('l') == False

def test_get_word_with_blanks() -> None:
    word = Word('cat')
    assert word.get_word_with_blanks() == '_ _ _'

def test_get_word_with_some_blanks() -> None:
    word = Word('cat')
    word.is_letter_in_word('a')
    assert word.get_word_with_blanks() == '_ a _'

def test_print_current_word() -> None:
    word = Word('cat')
    word.is_letter_in_word('a')
    assert str(word) == '_ a _'

def test_equals() -> None:
    word = Word('dog')
    assert word == Word('dog')
    assert not word == Word('cat')

def test_word_has_blanks() -> None:
    word = Word('dog')
    assert word.word_has_blanks()
