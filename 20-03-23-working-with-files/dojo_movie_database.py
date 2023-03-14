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


movie_data = open('movie_data.txt', 'r+')
lines = movie_data.readlines()
title_lines = []
for i in range(1, 20, 4):
    print(i)
    title_lines.append(i)
print(title_lines)
movie_data.close()