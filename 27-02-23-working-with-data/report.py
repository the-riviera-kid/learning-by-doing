import movie_data

def main():
    movies = movie_data.movies
    number_of_movies = count_movies(movies)
    average_rating = get_average_rating(movies)
    best_movie = get_best_movie(movies)
    worst_movie = get_worst_movie(movies)
    print(f'Total number of movies: {number_of_movies}')
    print(f'Average rating of movies: {average_rating}')
    print(f'Best movie: "{best_movie}"')
    print(f'Worst movie: "{worst_movie}"')

def count_movies(movies):
    return len(movies)

def get_average_rating(movies):
    ratings = [get_rating(x) for x in movies]
    return sum(ratings) / len(ratings)

def get_best_movie(movies):
    best = max(movies, key=get_rating)
    return best['title']

def get_worst_movie(movies):
    worst = min(movies, key=get_rating)
    return worst['title']

def get_rating(movie):
    return movie['rating']

if __name__ == '__main__':
    main()
