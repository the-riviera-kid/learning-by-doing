def main():
    target = get_target_word()
    guesses = []
    guesses_remaining = 6
    unsolved = True
    while guesses_remaining and unsolved:
        print(f'You have {guesses_remaining} guesses remaining')
        guess = input(f'Guess this: {blankify(target, guesses)}: ')
        guesses.append(guess)
        guesses_remaining -= 0 if guess in target else 1 
        unsolved = not blankify(target, guesses) == target

    if unsolved:
        print(f'Aw shucks. You were looking for {target}.')
    else:
        print(f'Noooooice!. You had {guesses_remaining} guesses remaining.')

def blankify(target, guesses):
    return ''.join([x if x in guesses else '_' for x in target])

def get_target_word():
    return 'aggregate'
        



if __name__=='__main__':
    main()
