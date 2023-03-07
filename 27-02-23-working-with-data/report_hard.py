'''
    This program will import the movie data, and print the following information to the screen:

    Actor appearring in most movies: Julia Roberts
    Actor with best average rating: Jean Claude Van 
        - Get all the actors
        - Attach actors to the rating
        - if actors appear in more than 1 movie, get the average rating
        - Find the highest rating and print the actor
    Least popular genre in the 1980's: music videos
'''

import movie_data


def main():
    movie_list = movie_data.movies
    actor_appearring_in_most_movies(movie_list)
    actor_with_best_rating = best_rated_actor(movie_list)
    print('\nThe actors with best average ratings are:')
    for actor in actor_with_best_rating:
        print(actor)
    least_popular = least_popular_genre_in_1980s(movie_list)
    print(f'\nThe least popular genre in the 1980s was {least_popular}', end='\n\n')


def actor_appearring_in_most_movies(movie_list):
    movie_actor_dict = {}
    movie_actors = []
    for movie in movie_list:
        actors = movie.get('actors')
        for actor in actors:
            movie_actors.append(actor)
    for actor in movie_actors:
        movie_actor_dict[actor] = movie_actors.count(actor)
    most_frequent_actor = max(movie_actor_dict, key=movie_actor_dict.get)
    print(f'\nThe actor appearing in the most movies is {most_frequent_actor}')


def best_rated_actor(movie_list):
    actor_dict = {}
    for movie in movie_list:
        for actor in movie['actors']:
            if actor in actor_dict:
                actor_dict[actor].append(movie['rating'])
            else:
                actor_dict[actor] = [movie['rating']]
    for actor, rating_list in actor_dict.items():
        actor_dict[actor] = sum(rating_list)//len(rating_list)
    best_actor_list = []
    for actors, rating in actor_dict.items():
        if rating == max(actor_dict.values()):
            best_actor_list.append(actors)
    return best_actor_list


def least_popular_genre_in_1980s(movie_list):
    genres = []
    genres_1980s = []
    for movie in movie_list:
        genre = movie['genre']
        genres.append(genre)
        year = movie['year']
        if year >= 1980 and year < 1990:
            genres_1980s.append(genre)
    genre_dict = {}
    for genre in genres:
        number = genres_1980s.count(genre)
        genre_dict[genre] = number
    least_popular = min(genre_dict, key=genre_dict.get)
    return least_popular


if __name__ == '__main__':
    main()
