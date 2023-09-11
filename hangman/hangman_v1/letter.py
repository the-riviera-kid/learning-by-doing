class Letter:
    def __init__(self, letter: str) -> None:
        self._letter = letter
        self._letter_or_blank = self._get_letter_or_blank()

    def _get_letter_or_blank(self) -> None:
        pass