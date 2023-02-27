'''
    This program will import the movie data, and print the following information to the screen:

    Total number of movies: 231
    Average rating of movies: 2.7
    Best movie: "2 Fast 2 Furious"
    Worst movie: "Citizen Kane"
'''

import movie_data


def main():
    movie_list = movie_data.movies
    print_total_number_of_movies(movie_list)
    print_avg_rating_of_movies(movie_list)
    print_best_movie(movie_list)
    print_worst_movie(movie_list)


def print_total_number_of_movies(movie_list):
    print(f'There are {len(movie_list)} movies in total.')


def print_avg_rating_of_movies(movie_list):
    ratings = []
    for movie in movie_list:
        ratings.append(movie.get('rating'))
    average = sum(ratings)/len(ratings)
    print(f'The average rating is {average}')


def print_best_movie(movie_list):
    movie_ratings = {}
    for movie in movie_list:
        movie_ratings[movie.get('title')] = movie.get('rating')
    best_movie = max(movie_ratings, key=movie_ratings.get)
    print(f'The best movie is {best_movie}')


def print_worst_movie(movie_list):
    movie_ratings = {}
    for movie in movie_list:
        movie_ratings[movie.get('title')] = movie.get('rating')
    worst_movie = min(movie_ratings, key=movie_ratings.get)
    print(f'The worst movie is {worst_movie}')


if __name__ == '__main__':
    main()

