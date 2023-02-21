import random

def main():
    target = get_target_word()
    guesses = []
    guesses_remaining = 6
    unsolved = True
    print(get_hangman_string(guesses_remaining))
    while guesses_remaining and unsolved:
        guesses, guesses_remaining, unsolved = play_round(guesses_remaining, target, guesses)
    report(guesses_remaining, target, unsolved)

def report(guesses_remaining, target, unsolved):
    if unsolved:
        print(f'Aw shucks. You were looking for {target}.')
    else:
        print(f'Noooooice!. You had {guesses_remaining} guesses remaining.')

def play_round(guesses_remaining, target, guesses):
    print(f'You have {guesses_remaining} guesses remaining')
    guess = input(f'Guess this: {blankify(target, guesses)}: ')
    guesses.append(guess)
    guesses_remaining -= 0 if guess in target else 1 
    unsolved = not blankify(target, guesses) == target
    print('\n\n' + get_hangman_string(guesses_remaining))
    return guesses, guesses_remaining, unsolved

def blankify(target, guesses):
    return ''.join([x if x in guesses else '_' for x in target])

def get_target_word():
    words = ['aggregate', 'syncopation', 'mastication', 'piloerection', 'breakdown', 'extricate', 'queen', 'quiz', 'equality',
             'animosity', 'glitters', 'glistens', 'growling', 'fortitude', 'resonance', 'ape', 'spy', 'dog', 'cat', 'bat', 'bar']
    return random.choice(words)

def get_hangman_string(guesses_remaining):
    mods = [(3, 4, '\\'), (3, 2, '/'), (2, 2, '-'), (2, 4, '-'), (2, 3, 'O'), (1, 3, 'o')]
    data = get_hangman_data_base()
    for i in range(guesses_remaining, len(mods)):
        y, x, char = mods[i]
        data[y][x] = char
    return '\n'.join(''.join(row) for row in data)

def get_hangman_data_base():
    return [
    	['/', '-', '-', '-', ' '],
    	['|', ' ', ' ', ' ', ' '],
    	['|', ' ', ' ', ' ', ' '],
    	['|', ' ', ' ', ' ', ' '],
    	['|', ' ', ' ', ' ', ' '],
    	['|', '_', '_', '_', '_'],
    ]


if __name__=='__main__':
    main()
