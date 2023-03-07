'''
    This program will import the movie data, and print the answer to the following question.
        The answer is one single movie title, with double quotes. 
        
    The question is:
        Matthew Broderick sucks. He makes every movie one point worse.
        Judd Nelson is harsh. He makes every movie one point better. 
        Moreover, he's so cool, that his coolness is contagious and does not obey the laws of space-time. 
        Anyone who has ever been in a movie with Judd Nelson, makes every other movie they're in one point better. 
        With all that in mind: 
        
        What's the best Ally Sheedy movie?


        Brain Storm:
            Matthew Broderick -> movie_rating -1
            Judd Nelson -> movie_rating +1
            if Judd Nelson in actors_list -> for each actor in that list -> find all the movies they acted in and +1 to the rating of that movie.

            Find all Ally Sheedy movies and get the highest rated
'''

import movie_data


def main():
    movie_list = movie_data.movies
    matthew_movie_list = matthew_broderick_minus_one(movie_list)
    judd_movie_list = judd_nelson_plus_one(matthew_movie_list)
    judd_nelson_actors(judd_movie_list)


def matthew_broderick_minus_one(movie_list):
    matthew_movie_list = []
    for movie in movie_list:
        if 'Matthew Broderick' in movie['actors']:
            movie['rating'] -= 1
            matthew_movie_list.append(movie)
        else:
            matthew_movie_list.append(movie)
    return matthew_movie_list


def judd_nelson_plus_one(matthew_movie_list):
    judd_movie_list = []
    for movie in matthew_movie_list:
        if 'Judd Nelson' in movie['actors']:
            movie['rating'] += 1
            judd_movie_list.append(movie)
        else:
            judd_movie_list.append(movie)
    return judd_movie_list


def judd_nelson_actors(judd_movie_list):
    judd_actors = []
    for movie in judd_movie_list:
        if 'Judd Nelson' in movie['actors']:
            for actor in movie['actors']:
                judd_actors.append(actor)
    # Remove Judd from the list of Judd actors
    remove_judd = judd_actors.count('Judd Nelson')
    for i in range(remove_judd):
        judd_actors.remove('Judd Nelson')
    return judd_nelson_actors_plus_one(judd_actors, judd_movie_list)


def judd_nelson_actors_plus_one(judd_actors, judd_movie_list):
    plus_one_list = []
    for movie in judd_movie_list:
        for actor in judd_actors:
            if actor in movie['actors'] and 'Judd Nelson' not in movie['actors']:
                movie['rating'] += 1
        else:
            plus_one_list.append(movie)
    return best_ally_sheedy_movie(plus_one_list)


def best_ally_sheedy_movie(plus_one_list):
    ally_dict = {}
    for movie in plus_one_list:
        if 'Ally Sheedy' in movie['actors']:
            ally_dict[movie['title']] = movie['rating']
    for movie, rating in ally_dict.items():
        if rating == max(ally_dict.values()):
            print(f'The best Ally Sheedy movie is {movie} with a rating of {rating}')


if __name__ == '__main__':
    main()

