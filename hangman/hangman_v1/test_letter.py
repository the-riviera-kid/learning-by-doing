from letter import Letter


def test_letter() -> None:
    assert Letter('a')

def test_letter_or_blank() -> None:
    word = 'cat'
    assert Letter('a') == 'a'
