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

class Celcius:
    def __init__(self, temp):
        self.temp = temp

    def __eq__(self, other):
        return self.temp == other._to_celcius().temp
    
    def __add__(self, other):
        return Celcius(self.temp + other.temp)
    
    def _to_celcius(self):
        return self
    

class Fahrenheit:
    def __init__(self, temp):
        self.temp = temp

    def __eq__(self, other):
        return self._to_celcius() == other._to_celcius()
    
    def _to_celcius(self):
        celcius_value = (self.temp - 32)/1.8
        return Celcius(celcius_value)