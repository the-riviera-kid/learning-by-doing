import dojo_movie_database_2


def main():
    with open('movie_data.txt', 'r') as movie_txt_data:
        movie_data = movie_txt_data.readlines()
        movie_data = [i.strip() for i in movie_data]
        movies = [movie_data[i:i+5] for i in range(0, len(movie_data), 5)]
        movie_list = create_dict(movies)
    dojo_movie_database_2.main_dojo(movie_list)


def create_dict(movies):
    keys = ['title', 'actors', 'year', 'genre', 'rating']
    movies = [dict(zip(keys, movie)) for movie in movies]
    for movie in movies:
        movie['actors'] = movie['actors'].split(', ')
    return movies


def update_txt_file(title, actors, year, genre, rating):
    with open('movie_data.txt', 'a') as movie_txt_data:
        actors = ', '.join(actors)
        movie_txt_data.write(title + '\n' + actors + '\n' + str(year) + '\n' + genre + '\n' + str(rating) + '\n')


if __name__ == '__main__':
    main()