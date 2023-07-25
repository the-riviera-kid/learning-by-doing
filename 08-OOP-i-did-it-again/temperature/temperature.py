'''
Get the mean average temperature from various temperature units

Class Celcius
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

Class Fahrenheit
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

Class Kelvin
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

'''

# def avg_temp(temps):
#     return sum(temps, Celcius(0))/len(temps)


class Kelvin:
    def __init__(self, temp): # self == Kelvin, temp == int
        self.temp = temp # self.temp == int
        # returns None

    def __eq__(self, other): # self == Kelvin, other == Kelvin
        return self.temp == other.temp # self.temp == int, other.temp == int
        # returns True or False        # int(50) == int(50)
    
    def __add__(self, other): # self == Kelvin, other == Kelvin
        return Kelvin(self.temp + other.temp) # self.temp == int, other.temp == int
        # returns int -> int(50) -> Kelvin(50)

    def __floordiv__(self, divisor):
        return Kelvin(self.temp // divisor)
    