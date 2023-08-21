from report import Movie
import pytest

def test_it_works():
    assert True == True

def test_class_attributes():
    result = Movie('Spider-Man', ['Maguire'], 2002, 'action', 8)
    assert result.title == 'Spider-Man'
    assert result.actors == ['Maguire']
    assert result.year == 2002
    assert result.genre == 'action'
    assert result.rating == 8

def test_string_method_works():
    result = Movie('Spider-Man', ['Maguire'], 2002, 'action', 8).__str__()
    assert result == 'Spider-Man, 8'

def test_less_than_method_works():
    movie1 = Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7)
    movie2 = Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9)
    assert movie1 < movie2

def test_less_than_method_works_false():
    movie1 = Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7)
    movie2 = Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9)
    assert not movie2 < movie1

def test_less_than_method_again():
    movie1 = Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7)
    movie2 = Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9)
    with pytest.raises(TypeError):
        assert not movie2 < 19