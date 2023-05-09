def check_if_invalid(user_input):
    if user_input is None or not str(user_input).isalpha():
        return 'Sorry that is invalid'


def build_word_grid(word):
    word_list = [] # ['Pot', 'pOt', 'poT']
    for i in range(len(word)): # i = [0] -> p
        previous_letters_lower = word[:i].lower() # slice from [0] -> [0]
        capital_letter = word[i].upper() # [0] -> P
        last_letters_lowered = word[i+1:].lower() # slice from [1] -> end
        word = previous_letters_lower + capital_letter + last_letters_lowered
        word_list.append(word)
    return word_list # ['Pot', 'pOt', 'poT']