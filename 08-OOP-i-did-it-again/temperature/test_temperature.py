# from temperature import avg_temp


# def test_temperature_func_exists():
#     assert avg_temp

# def test_avg_1_temp():
#     result = avg_temp([2])
#     assert result == 2

# def test_avg_2_temps():
#     result = avg_temp([2, 4])
#     assert result == 3

# def test_avg_2_temps_celc_faren():
#     result = avg_temp([Celcius(0), Fahrenheit(32)])
#     assert result == Celcius(0)

'''
result = avg_temp([Celcius(0), Fahrenheit(32)])
result = avg_temp([celcius object 0, Fahrenheit(32)])
result = avg_temp([celcius object 0, farehnheit object 32]) -> returns a celcuis object

'''

from temperature import Kelvin

def test_create_kelvin():
    assert Kelvin(0)

def test_compare_kelvin():
    assert Kelvin(42) == Kelvin(42)

def test_adding_kelvins():
    result = Kelvin(20) + Kelvin(30)
    assert result == Kelvin(50)

def test_dividing_kelvin():
    result = Kelvin(100) // 2
    assert result == Kelvin(50)