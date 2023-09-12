from word import Word
from typing import Any

import random

class WordCollection:
    def __init__(self, word_list: 'list[str]') -> None:
        self.word_list = word_list
        self.word = self.get_random_word()
        
    def get_random_word(self) -> object:
        random_word = random.choice(self.word_list)
        return Word(random_word)
