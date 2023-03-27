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
    game = random.choices(quiz_data, k=5)
    score = 0
    score = play_game(game, score)
    print(f'Final score: {score}')
    return score


def intro():
    high_score = file_handling.get_high_score_data()
    if high_score == ['0', 'nobody']:
        print(f'There is no high score. Be the first to set one!')
    else:
        print(f'The high score is {high_score[0]}, set by {high_score[1]}')


def play_game(game, score):
    for round in game:
        game_answer = game_round(round)
        score = compare_user_guess(game_answer, score)
    return score


def game_round(round):
    game_question = round['question']
    print(game_question)
    game_choices = round['choices']
    game_answer = round['answer']
    for k, v in game_choices.items():
        print(k, v)
        if v == game_answer:
            game_answer = k[0]
    return game_answer


def compare_user_guess(game_answer, score):
    user_answer = input('Your Guess? > ')
    if user_answer.upper() == game_answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    return score





# =======================================================

def print_only_questions(quiz_data):
    questions = []
    for quiz in quiz_data:
        questions.append(quiz['question'])
    print(f'The questions are {questions}')
