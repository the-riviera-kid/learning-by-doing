# Actor appearing in most movies
# Actor with best average rating
# Least popular genre in the 1980s
#
import movie_data

def main():
    print(f'Actor appearing in most movies: {get_popular_actor(movie_data.movies)}')

def get_popular_actor(movies):
    actor_count = {}
    for movie in movies:
        for actor in movie['actors']:
            actor_count[actor] = 1 + actor_count[actor] if actor in actor_count else 0
    return max(actor_count, key=actor_count.get)

if __name__ == '__main__':
    main()
