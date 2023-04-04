def blank(target_word, characters):
    if not isinstance(target_word, str):
        raise TypeError('This is no good for hangman!')
    if target_word:
        if characters:
            return ''.join(x if x in characters else '_' for x in target_word)
        else:
            return '_' * len(target_word)
    else:
        return ''