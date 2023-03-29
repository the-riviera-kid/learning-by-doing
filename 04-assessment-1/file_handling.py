import trivia_data


def get_quiz_data():
    with open('questions.txt', 'r') as quiz_txt_data:
        quiz_data = quiz_txt_data.readlines()
        quiz_data = [i.strip() for i in quiz_data] # turns txt into a list of strings -> each line is a string
        quiz_data = [quiz_data[i:i+3] for i in range(0, len(quiz_data), 3)] # list of lists -> every 3 lines is a list containing the 'question', 'choices' & 'answer'
        quiz_data = trivia_data.questions_list(quiz_data) # list of dictionaries. Uses the 3 indexes of each list as arguments to a function that creates dictionaries out of them
        quiz_data = trivia_data.make_dict_for_choices(quiz_data) # changes the 2nd item in the dict ('choices') from a list to a dictionary, randomizing the choices
    return quiz_data


def get_high_score_data():
    with open('high_score.txt', 'r') as high_score_data:
        high_score = high_score_data.readlines()
        high_score = [i.split(' ') for i in high_score] # a list of lists [['0', 'nobody']]
        high_score = high_score[0]
    return high_score


def update_high_score(score, high_score):
    if score >= int(high_score[0]):
        name = input('You set the high score! What is your name? > ')
        with open('high_score.txt', 'w+') as high_score_data:
            high_score[0] = score
            high_score[1] = name
            high_score_data.write(str(f'{high_score[0]} {high_score[1]}'))

