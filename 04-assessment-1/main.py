import itertools
import random


QUESTION_PATH = './questions.txt'
CARDS_PER_GAME = 5

class Card():
    def __init__(self, question, choices, answer):
        self.question = question
        choices = [x.strip() for x in choices.split(',')]
        self.choices = random.sample(choices, k=len(choices))
        self.answer = answer
        self._correct_index = self.choices.index(self.answer)
        self._selectors = ['a', 'b', 'c', 'd']
        self._lookup = {v: i for i, v in enumerate(self._selectors)}

    def _index_to_char(self, index):
        return self._selectors[index]

    def _char_to_index(self, char):
        c = char.strip().lower()
        return self._lookup[c]

    def render(self):
        lines = [
            f'{self.question}',
            f'{self._index_to_char(0).upper()}. {self.choices[0]}',
            f'{self._index_to_char(1).upper()}. {self.choices[1]}',
            f'{self._index_to_char(2).upper()}. {self.choices[2]}',
            f'{self._index_to_char(3).upper()}. {self.choices[3]}',
        ]
        return '\n'.join(lines)


    def is_guess_correct(self, guess):
        clean = guess.strip().lower()
        if clean in self._selectors:
            return self._char_to_index(clean) == self._correct_index
        else:
            return False

    def __str__(self):
        return f'{self.question} ({self.answer})'

def main():
    cards = load_cards()
    hand = random.sample(cards, k=CARDS_PER_GAME)
    score = 0
    for card in hand:
        print(card.render())
        player_answer = input("Your guess? > ")
        score += 1 if card.is_guess_correct(player_answer) else 0
    print(f'Final score: {score}')

def load_cards():
    cards = []
    with open(QUESTION_PATH, 'r') as f:
        for chunk in chunks(f, 3):
            question, answers, answer = stripper(chunk)
            cards.append(Card(question, answers, answer))

    return cards


def stripper(it):
    return (x.strip() for x in it)

def chunks(x, n):
    args = [iter(x)] * n
    return zip(*args)

if __name__ == '__main__':
    main()
