'''
    Challenge:
    Make a game where you ask the player some quiz questions.
    Check their answers
    Score them
    Keep a high score for the next game

    Order of txt in questions.txt:
    1. The text of the actual question
    2. A list of possible answers, separated by commas
    3. The correct answer

    You will need to:
    Read questions.txt file
    Parse it into a list of records
    Each record represents a question, with all its possible answers, and the correct solution
    Select five questions at random
    Display the high score and name of the high scorer
    Ask these questions to the player
    Show the question, and all four possible answers
    The answers must be in a random order
    The player should be able to enter something short to pick their answer (a b c d)
    After the player has answered five questions, display their score
    If their score is higher than or equal to the high score, they get to enter their name
    Display name with the high scorer at the start of the next run of the program.
'''

import file_handling
import random


def trivia_main(quiz_data):
    intro()
    game = random.choices(quiz_data, k=5) # get 5 random dictionaries from quiz_data list
    score = 0
    score = play_game(game, score) # gets a new score
    print(f'Final score: {score}')
    return score


def intro():
    high_score = file_handling.get_high_score_data() # high_score is a single list ['0', 'nobody']
    if high_score == ['0', 'nobody']:
        print(f'There is no high score. Be the first to set one!')
    else:
        print(f'The high score is {high_score[0]}, set by {high_score[1]}')


def play_game(game, score):
    for round in game: # for each of the 5 dictionaries
        game_answer = game_round(round) # returns the answer by letter
        score = compare_user_guess(game_answer, score) # sets a new score using the old score and the returned answer from previous function call
    return score


def game_round(round):
    print(round['question'])
    for letter, choice in round['choices'].items():
        print(letter, choice) # prints a multiple choice
        if choice == round['answer']: # if correct
            round['answer'] = letter[0] # 'answer' is key and 'letter' is value -> ('A.' - get 'A' without the '.') => {'answer': 'A'}
    return round['answer']


def compare_user_guess(game_answer, score):
    user_answer = input('Your Guess? > ')
    if user_answer.upper() == game_answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    return score
