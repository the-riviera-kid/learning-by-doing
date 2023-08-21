class Movie:
    def __init__(self, title, actors, year, genre, rating):
        self.title = title
        self.actors = actors
        self.year = year
        self.genre = genre
        self.rating = rating
    
    def __str__(self):
        return f'{self.title}, {self.year}, rated {self.rating} out of 10.'


spiderman = Movie('Spider-Man', ['Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco'], 2002, 'Action', 7)
print(spiderman)

movies = [
    Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7),
    Movie("Star Wars Episode I: The Phantom Menace", ["Liam Neeson", "Ewan McGregor", "Natalie Portman", "Jake Lloyd", "Brian Blessed"], 1999, "science fiction", 3),
    Movie("Star Trek IV: The Voyage Home", ["William Shatner", "Leonard Nimoy", "Michelle Nichols"], 1986, "science fiction", 8),
    Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9),
    Movie("The Naked Gun: From The Files Of Police Squad!", ["Leslie Nielsen", "O. J. Simpson", "Priscilla Presley"], 1988, "comedy", 8),
    Movie("Leprechaun", ["Warwick Davis", "Jennifer Aniston"], 1993, "horror", 6),
    Movie("Leprechaun 4: In Space", ["Warwick Davis"], 1996, "horror", 10),
    Movie("Flash Gordon", ["Brian Blessed", "Timothy Dalton", "Max von Sydow"], 1980, "science fiction", 6),
    Movie("The Rock", ["Nicolas Cage", "Sean Connery", "Ed Harris", "Michael Biehn"], 1996, "action", 8),
    Movie("Con Air", ["Nicolas Cage", "John Malkovich", "John Cusack", "Steve Buscemi", "Ving Rhames"], 1997, "action", 9),
    Movie("Airheads", ["Brendan Fraser", "Adam Sandler", "Steve Buscemi", "Judd Nelson", "Lemmy Kilmister"], 1994, "comedy", 5),
    Movie("The Breakfast Club", ["Judd Nelson", "Emilio Estevez", "Ally Sheedy", "Molly Ringwald"], 1985, "drama", 6),
    Movie("Wargames", ["Matthew Broderick", "Ally Sheedy"], 1983, "drama", 8),
    Movie("Godzilla", ["Matthew Broderick", "Jean Reno"], 1998, "action", 6),
    Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 9),
]

for movie in movies:
    print(movie)