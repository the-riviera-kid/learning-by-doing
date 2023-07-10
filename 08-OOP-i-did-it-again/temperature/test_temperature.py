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

# def test_celcius_fahrenheit_calc():
#     result = calc_conversion(0)
#     assert result == 32

from temperature import Celcius, Fahrenheit

def test_create_celcius():
    assert Celcius(72)

def test_compare_celcius():
    assert Celcius(20) == Celcius(20)

def test_compare_celcius_different():
    assert not Celcius(20) == Celcius(30)

def test_adding_celcius():
    result = Celcius(10) + Celcius(20)
    assert result == Celcius(30)

def test_create_fahrenheit():
    assert Fahrenheit(63)

def test_compare_farhenheit():
    assert Fahrenheit(50) == Fahrenheit(50)

def test_compare_fahrenheit_with_celcius():
    assert Fahrenheit(32) == Celcius(0)

def test_compare_celcius_with_fahrenheit():
    assert Celcius(0) == Fahrenheit(32)

def test_adding_fahrenheit():
    assert Fahrenheit(10) + Fahrenheit(22) == Fahrenheit(32)

def test_adding_fahrenheit_to_celcius():
    assert Fahrenheit(32) + Celcius(0) == Fahrenheit(32)