class Word:
    def __init__(self, word: str) -> None:
        self.word = word
        self.guessed_letters: list[str] = []
        self.current_word = self.get_word_with_blanks()
        self.has_blanks = self.word_has_blanks()

    def is_letter_in_word(self, letter: str) -> bool:
        self.guessed_letters.append(letter)
        self.current_word = self.get_word_with_blanks()
        return letter in self.word
    
    def get_word_with_blanks(self) -> str:
        word_with_blanks = self.word # ''
        for letter in self.word: # 'cat'
            if letter not in self.guessed_letters: # []
                word_with_blanks = word_with_blanks.replace(letter, '_')
        word_with_blanks = ' '.join(word_with_blanks)
        return word_with_blanks # '_ a _'
    
    def __str__(self) -> str:
        return f'{self.current_word}'
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Word):
            return self.word == other.word
        raise NotImplementedError()
    
    def word_has_blanks(self) -> bool:
        return '_' in self.current_word
