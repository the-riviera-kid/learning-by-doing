import file_handling
import random


# create a dictionary for each question
def question(question, choices, answer):
    return {
    	"question": question,
    	"choices": choices.split(', '),
    	"answer": answer
    }


# create a list of dictionaries
def questions_list(quiz_data):
    questions = [question(i[0], i[1], i[2]) for i in quiz_data] # uses the 3 indexes of each list as arguments to a function that creates dictionaries out of them (calls the function above)
    return questions


def make_dict_for_choices(quiz_data):
    '''
        Changes the 2nd item in the dict ('choices') from a list to a dictionary.
    '''
    multi_choice = ['A.', 'B.', 'C.', 'D.']
    for quiz in quiz_data: # for dict in list
        random.shuffle(quiz['choices']) # randomize the list of choices every time
        choices = dict(zip(multi_choice, quiz['choices'])) # make a dict using 'multi_choice' list as keys & 'quiz' dict 'choices' value (list of choices) as values
        quiz['choices'] = choices # where the key in 'quiz' dict is 'choices' -> value is now a dict
    return quiz_data


'''
    [
        {'question': 'Berlin is the capital of which country?', 'choices': {'A': 'Germany', 'B': 'France', 'C': 'Italy', 'D': 'Outer Mongolia'}, 'answer': 'Germany'}, 
        {'question': 'In computer graphics, what do the letters VDU stand for?', 'choices': {'A': 'Vertex Data Unit', 'B': 'Vertex Data Unscrambler', 'C': 'Visual Display Unit', 'D': 'Very Depressed Users'}, 'answer': 'Visual Display Unit'}, 
        {'question': 'In chess, which of these is *not* a valid move?', 'choices': {'A': 'En passant', 'B': 'Castling', 'C': 'Promoting', 'D': 'Demoting'}, 'answer': 'Demoting'}, 
        {'question': 'Are global variables a good idea?', 'choices': {'A': 'Yes', 'B': 'No', 'C': 'Maybe', 'D': 'It depends'}, 'answer': 'No'}, 
        {'question': 'Are global variables a good idea?', 'choices': {'A': 'No', 'B': 'No', 'C': 'No', 'D': 'No'}, 'answer': 'No'}, 
        {'question': 'How many toes does a horse have on each foot?', 'choices': {'A': 'One', 'B': 'Three', 'C': 'Five', 'D': 'Six'}, 'answer': 'One'}, 
        {'question': 'What does a Manx Cat not have?', 'choices': {'A': 'Toes', 'B': 'Ears', 'C': 'Tail', 'D': 'A Face'}, 'answer': 'Tail'}, 
        {'question': 'The Japanese poetry form consisting of three lines, with 5, 7 and 5 syllables respectively, is called...?', 'choices': {'A': 'Takoyaki', 'B': 'Haiku', 'C': 'Kaiju', 'D': 'Nandeska'}, 'answer': 'Haiku'}, 
        {'question': 'What makes Gazpacho soup unusual?', 'choices': {'A': "It's illegal in the EU", 'B': "It's served cold", 'C': 'It contains live fish', 'D': "It's served in an eggshell"}, 'answer': "It's served cold"}, 
        {'question': 'In the 90\'s sitcom "Friends", who was Monica\'s brother?', 'choices': {'A': 'Chandler', 'B': 'Joey', 'C': 'Ross', 'D': 'Gunther'}, 'answer': 'Ross'}, 
        {'question': 'Who is the best actor?', 'choices': {'A': 'Robert Stack', 'B': 'Matthew Broderick', 'C': 'Judd Nelson', 'D': 'Leslie Nielsen'}, 'answer': 'Judd Nelson'}, 
        {'question': 'The Dutch are the only people to ever have...?', 'choices': {'A': 'Conquered Mars', 'B': 'Enjoyed licorice', 'C': 'Gained immortality', 'D': 'Eaten their Prime Minister'}, 'answer': 'Eaten their Prime Minister'}, 
        {'question': 'Which of these is *not* a real unit of measurement *really* used by the British?', 'choices': {'A': 'Hectare', 'B': 'Hand', 'C': 'Arm', 'D': 'Hundredweight'}, 'answer': 'Arm'}, 
        {'question': 'What does the Morse Code signal "...---..." mean?', 'choices': {'A': 'IFI', 'B': 'IKI', 'C': 'SOS', 'D': 'FKU'}, 'answer': 'SOS'}, 
        {'question': "How many people were onboard Amelia Earhart's aircraft when it disappeared?", 'choices': {'A': '0', 'B': '1', 'C': '2', 'D': '3'}, 'answer': '2'}, 
        {'question': "Who was the Director of Software Engineering for NASA's Apollo Program?", 'choices': {'A': 'Steve Jobs', 'B': 'Margaret Hamilton', 'C': 'Donald Knuth', 'D': 'Edgar Dijkstra'}, 'answer': 'Margaret Hamilton'}, 
        {'question': "Dan's middle name is...?", 'choices': {'A': '"Ger"', 'B': 'Malcolm', 'C': 'A closely guarded secret', 'D': 'Samuel'}, 'answer': 'A closely guarded secret'}, 
        {'question': 'The inventory of the Python programming language is...?', 'choices': {'A': 'Dutch', 'B': 'Irish', 'C': 'Dutch-Irish', 'D': 'A bastard'}, 'answer': 'Dutch'}, 
        {'question': 'The word "arachnids" covers which type of animals?', 'choices': {'A': 'Scorpions', 'B': 'Snakes', 'C': 'Cockroaches', 'D': 'Crabs'}, 'answer': 'Scorpions'}, 
        {'question': 'Which German rock band finally knocked Bryan Adams off the top of the UK pop charts after 16 weeks?', 'choices': {'A': 'Rammstein', 'B': 'Die Toten Hosen', 'C': 'Scorpions', 'D': 'Guano Apes'}, 'answer': 'Scorpions'}, 
        {'question': 'Complete this sentence: "I ain\'t afraid of no ... "?', 'choices': {'A': 'Goats', 'B': 'Grues', 'C': 'Ghosts', 'D': 'Goals'}, 'answer': 'Ghosts'}, 
        {'question': 'What is 4 - 2 * 6 ?', 'choices': {'A': '12', 'B': '16', 'C': '-12', 'D': '-8'}, 'answer': '-8'}, 
        {'question': 'Including both land and maritime borders, how many countries border the Netherlands?', 'choices': {'A': '2', 'B': '3', 'C': '4', 'D': '6'}, 'answer': '4'}, 
        {'question': 'What is the chemical formula for water?', 'choices': {'A': 'H2SO4', 'B': 'O3', 'C': 'H2O', 'D': 'R2D2'}, 'answer': 'H2O'}, 
        {'question': 'Which extreme metal band has the world record for "shortest song" with their track "You Suffer"?', 'choices': {'A': 'Napalm Death', 'B': 'Fleshgod Apocalypse', 'C': 'Cannibal Corpse', 'D': 'Party Cannon'}, 'answer': 'Napalm Death'}, 
        {'question': "If you were 'treading the boards', where would you be?", 'choices': {'A': 'Underwater', 'B': 'On stage', 'C': 'Breaking and entering', 'D': 'In a car'}, 'answer': 'On stage'}, 
        {'question': 'According to Shakespeare, what is the soul of wit?', 'choices': {'A': 'Irony', 'B': 'Brevity', 'C': 'Subtlety', 'D': 'Bodily noises'}, 'answer': 'Brevity'}, 
        {'question': 'Which of the following would be appropriate to extinguish an oil fire?', 'choices': {'A': 'Water', 'B': 'Alcohol', 'C': 'A damp towel', 'D': 'An iguana'}, 'answer': 'A damp towel'}, 
        {'question': '"The Hitchhiker\'s Guide to the Galaxy" was written by which British author?', 'choices': {'A': 'William Shakespeare', 'B': 'Oscar Wilde', 'C': 'Jane Austen', 'D': 'Douglas Adams'}, 'answer': 'Douglas Adams'}, 
        {'question': 'In "The Hitchhiker\'s Guide to the Galaxy", what is the answer to life, the universe, and everything?', 'choices': {'A': 'Kindness', 'B': 'The French', 'C': '42', 'D': 'A small Chilean sea slug called Gerald'}, 'answer': '42'}, 
        {'question': 'Where are the Islets of Langerhans?', 'choices': {'A': 'The South China Sea', 'B': 'Norway', 'C': 'Madagascar', 'D': 'The pancreas'}, 'answer': 'The pancreas'}, 
        {'question': 'Which mathematician invented a cellular automata known as "The Game of Life"?', 'choices': {'A': 'Wesley Beaver', 'B': 'Stephen Hawking', 'C': 'John Conway', 'D': 'Edgar Dijkstra'}, 'answer': 'John Conway'}, 
        {'question': 'What is the capital of Morocco?', 'choices': {'A': 'Sale', 'B': 'Marrakech', 'C': 'Rabat', 'D': 'Tangier'}, 'answer': 'Rabat'}, 
        {'question': 'What is the note interval between strings on a violin?', 'choices': {'A': 'Thirds', 'B': 'Fourths', 'C': 'Fifths', 'D': 'Sixths'}, 'answer': 'Fifths'}, 
        {'question': "In Squash, what is the name of the 'out' area at the bottom of the front wall?", 'choices': {'A': 'The Pot', 'B': 'The Jug', 'C': 'The Tin', 'D': 'The Chamberpot'}, 'answer': 'The Tin'}, 
        {'question': 'What is the name of the poetry technique where consecutive words start with the same letter?', 'choices': {'A': 'Assonance', 'B': 'Alliteration', 'C': 'Consonants', 'D': 'Insurance'}, 'answer': 'Alliteration'}, 
        {'question': 'What "p" word means "courteous; behaving in an expected manner"?', 'choices': {'A': 'Police', 'B': 'Politics', 'C': 'Polite', 'D': 'Poultice'}, 'answer': 'Polite'}, 
        {'question': 'Which of the following words describes cats?', 'choices': {'A': 'Bovine', 'B': 'Canine', 'C': 'Caprine', 'D': 'Feline'}, 'answer': 'Feline'}, 
        {'question': 'In Dungeons & Dragons, which of these classes would most benefit from a high Strength score?', 'choices': {'A': 'Rogue', 'B': 'Bard', 'C': 'Wizard', 'D': 'Fighter'}, 'answer': 'Fighter'}, 
        {'question': 'Wind is caused by...?', 'choices': {'A': 'Trees breathing', 'B': "Earth's rotation", 'C': 'Pressure differences', 'D': "Last night's beans"}, 'answer': 'Pressure differences'}
'''