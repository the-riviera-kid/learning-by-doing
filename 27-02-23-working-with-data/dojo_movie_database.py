'''
    dojo_movie_database.py : This program will import the movie data, and then provide a menu of options to the user. 
    The user can select an option, the program will do it, and afterwards the program should return to the main menu. 
    
    The options are:

    List : List the name and year of all movies, separated by a comma.
    Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
    Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
    Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. 
          This new movie should show up in the other searches.
    Quit : Ends the program.
'''

import movie_data


def main():
    movie_list = movie_data.movies
    main_menu = True
    while main_menu:
        menu_option = menu_options()
        option_choice = navigate(menu_option, movie_list, main_menu)
        print(option_choice)


def menu_options():
    option = input('\nWhat would you like to do?\
           \n\
           \nOption 1: Display all Movies\
           \nOption 2: Search Movies by Actor\
           \nOption 3: Search Movies by Genre\
           \nOption 4: Add Movie\
           \nOption 5: Quit\n\n')
    return option


def navigate(menu_option, movie_list, main_menu):
    if menu_option == '1':
        display_all_movies(movie_list)
        input('Press any key to return to the main menu ')
        return main_menu
    elif menu_option == '2':
        return 2
    elif menu_option == '3':
        return 3
    elif menu_option == '4':
        return 4
    else:
        exit()


def display_all_movies(movie_list):
    for movie in movie_list:
        title = movie['title']
        year = movie['year']
        print(f'{title}, {year}')


if __name__ == '__main__':
    main()