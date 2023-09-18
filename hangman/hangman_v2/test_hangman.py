from hangman import Hangman

def test_hangman_6_guesses() -> None:
    hangman = Hangman(6)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|",
                                     "|",
                                     "|",
                                     "|",
                                     "|________"])


def test_hangman_5_guesses() -> None:
    hangman = Hangman(5)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|",
                                     "|",
                                     "|",
                                     "|________"])

def test_hangman_4_guesses() -> None:
    hangman = Hangman(4)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|      |",
                                     "|      |",
                                     "|",
                                     "|________"])

def test_hangman_3_guesses() -> None:
    hangman = Hangman(3)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|     \|",
                                     "|      |",
                                     "|",
                                     "|________"])

def test_hangman_2_guesses() -> None:
    hangman = Hangman(2)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|     \|/",
                                     "|      |",
                                     "|",
                                     "|________"])

def test_hangman_1_guesses() -> None:
    hangman = Hangman(1)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|     \|/",
                                     "|      |",
                                     "|     /  ",
                                     "|________"])

def test_hangman_0_guesses() -> None:
    hangman = Hangman(0)
    assert str(hangman) == '\n'.join(["_________",
                                     "|      |",
                                     "|      O",
                                     "|     \|/",
                                     "|      |",
                                     "|     / \ ",
                                     "|________"])
