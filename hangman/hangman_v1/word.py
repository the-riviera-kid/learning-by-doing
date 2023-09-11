from letter import Letter
from typing import List
import random

class Word:
    def __init__(self, letter: str) -> None:
        self._word = self._generate_word()
        self.guessed_letter = letter
        self.display = self.check_guess_in_word()
        self.display = self.display_blanks_or_letters()

    def _generate_word(self) -> str:
        word_list = ['cat']
        return random.choice(word_list)
    
    def check_guess_in_word(self) -> str:
        display = []
        for letter in self._word:
            if self.guessed_letter == letter:
                display.append(letter)
            else:
                display.append('_')
        return ' '.join(display)
    
    def display_blanks_or_letters(self) -> str:
        return self.display

    def __str__(self) -> str:
        return self.display