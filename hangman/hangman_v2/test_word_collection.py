from word_collection import WordCollection
from word import Word

import random

def test_word_collection_with_word_list() -> None:
    my_word_list = WordCollection(['cat', 'dog'])
    assert len(my_word_list.word_list) == 2

def test_dog_in_word_list() -> None:
    my_word_list = WordCollection(['cat', 'dog'])
    assert 'dog' in my_word_list.word_list

def test_get_random_word() -> None:
    random.seed(1)
    my_word_list = WordCollection(['cat', 'dog'])
    random_word = my_word_list.get_random_word()
    assert random_word == Word('cat')