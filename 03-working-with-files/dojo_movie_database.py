'''
    Your mission this time is very similar to last time. We're going to be building the dojo_movie_database again! 
    However, there are two differences.

    1. You're not getting movie_data.py. This time, you're getting a text file, and you'll have to read that in, 
       and process the text into records yourself. It's the same movies in the same order, your queries should give the same answers. 
       However you'll have to read the file line by line, and put them in some sort of record structure.
    2. After you've added a movie to your database, you need to save that new movie to the text file. 
       If you add a movie, it needs to be visible in subsequent runs of your program.

    Now we've highlighted the differences, here's the specification:

    dojo_movie_database.py : 
    This program will import the movie data, and then provide a menu of options to the user. 
    The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
    List : List the name and year of all movies, separated by a comma.
    Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
    Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
    Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database. This new movie should show up in the other searches, every time the program is run.
    Quit : Ends the program.
'''

import os

def main():
    movie_data = open('movie_data.txt', 'r+')
    txt_lines = movie_data.readlines()
    keys_list = ['title_lines', 'actor_lines', 'year_lines', 'genre_lines', 'rating_lines']
    
    make_a_list_of_number_lists(txt_lines, keys_list)

    movie_data.close()


def make_a_list_of_number_lists(txt_lines, keys_list):
    big_list = []
    for num in range(1, 6):
        iteration = line_range(num, txt_lines)
        big_list.append(iteration)    
    return make_tuples(big_list, keys_list, txt_lines)


def line_range(start, txt_lines):
    s_list = []
    for i in range(start, len(txt_lines), 5):
        s_list.append(i)
    return s_list


def make_tuples(big_list, keys_list, txt_lines):
    lines_list = []
    lines_dict = dict(zip(keys_list, big_list))
    lines_list.append(lines_dict)
    # print(lines_list)
    # print(item['title_lines'])
    return get_txt_for_line_numbers(lines_list, txt_lines, lines_dict)


def get_txt_for_line_numbers(lines_list, txt_lines, lines_dict):
    # print(lines_dict)
    list_of_dicts = []
    # movie_details = {}
    for i in lines_dict['title_lines']:
        for num in range(len(lines_dict['title_lines'])):
            movie_details = {'title': i}
            # movie_details['actors'] = {i for i in lines_dict['actor_lines']}
    # for i in lines_dict['actor_lines']:
    #     for num in range(len(lines_dict['actor_lines'])):
    #         movie_details = {'actors': i}
 
        list_of_dicts.append(movie_details)
    print(list_of_dicts)
    
# for i in item['actor_lines']:
#     for num in range(len(item['actor_lines'])):
#         if 'actors' in movie_details:
#             movie_details['actors'] = i
#         else:
#             movie_details['actors'] = i

    # for line in lines_dict['title_lines']:
        # print(line)
        # movie_details['title'] = line
    # print(movie_details)
        # list_of_dicts.append(item_2)
        # print(list_of_dicts)
    # print(list_of_dicts)


if __name__ == '__main__':
    main()

'''
    big_list = [
        [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71], 
        [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72], 
        [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73], 
        [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74], 
        [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        ]

    keys_list = ['title_lines', 'actor_lines', 'year_lines', 'genre_lines', 'rating_lines']

    lines_dict = {
        'title_lines': [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71], 
        'actor_lines': [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72], 
        'year_lines': [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73], 
        'genre_lines': [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74], 
        'rating_lines': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        }

    in 'title_lines', get each txt line from the list of values

    create a new list of dictionaries ->

    [
        {'title': 'Star Wars Episode IV: A New Hope', 'actors': ['Mark Hamill', 'Harrison Ford', 'Carrie Fisher', 'Alec Guiness'], 'year': 1977, 'genre': 'science fiction', 'rating': 7}, 
        {'title': 'Star Wars Episode I: The Phantom Menace', 'actors': ['Liam Neeson', 'Ewan McGregor', 'Natalie Portman', 'Jake Lloyd', 'Brian Blessed'], 'year': 1999, 'genre': 'science fiction', 'rating': 3}, 
        {'title': 'Star Trek IV: The Voyage Home', 'actors': ['William Shatner', 'Leonard Nimoy', 'Michelle Nichols'], 'year': 1986, 'genre': 'science fiction', 'rating': 8}, 
        {'title': 'Airplane!', 'actors': ['Leslie Nielsen', 'Robert Stack', 'Lloyd Bridges'], 'year': 1980, 'genre': 'comedy', 'rating': 9}, 
        {'title': 'The Naked Gun: From The Files Of Police Squad!', 'actors': ['Leslie Nielsen', 'O. J. Simpson', 'Priscilla Presley'], 'year': 1988, 'genre': 'comedy', 'rating': 8}, 
        {'title': 'Leprechaun', 'actors': ['Warwick Davis', 'Jennifer Aniston'], 'year': 1993, 'genre': 'horror', 'rating': 6}, 
        {'title': 'Leprechaun 4: In Space', 'actors': ['Warwick Davis'], 'year': 1996, 'genre': 'horror', 'rating': 10}, 
        {'title': 'Flash Gordon', 'actors': ['Brian Blessed', 'Timothy Dalton', 'Max von Sydow'], 'year': 1980, 'genre': 'science fiction', 'rating': 6}, 
        {'title': 'The Rock', 'actors': ['Nicolas Cage', 'Sean Connery', 'Ed Harris', 'Michael Biehn'], 'year': 1996, 'genre': 'action', 'rating': 8}, 
        {'title': 'Con Air', 'actors': ['Nicolas Cage', 'John Malkovich', 'John Cusack', 'Steve Buscemi', 'Ving Rhames'], 'year': 1997, 'genre': 'action', 'rating': 9}, 
        {'title': 'Airheads', 'actors': ['Brendan Fraser', 'Adam Sandler', 'Steve Buscemi', 'Judd Nelson', 'Lemmy Kilmister'], 'year': 1994, 'genre': 'comedy', 'rating': 5}, 
        {'title': 'The Breakfast Club', 'actors': ['Judd Nelson', 'Emilio Estevez', 'Ally Sheedy', 'Molly Ringwald'], 'year': 1985, 'genre': 'drama', 'rating': 6}, 
        {'title': 'Wargames', 'actors': ['Matthew Broderick', 'Ally Sheedy'], 'year': 1983, 'genre': 'drama', 'rating': 8}, 
        {'title': 'Godzilla', 'actors': ['Matthew Broderick', 'Jean Reno'], 'year': 1998, 'genre': 'action', 'rating': 6}, 
        {'title': 'The Transformers: The Movie', 'actors': ['Peter Cullen', 'Frank Welker', 'Leonard Nimoy', 'Judd Nelson', 'Robert Stack', 'Orson Welles'], 'year': 1986, 'genre': 'action', 'rating': 9}]
'''


