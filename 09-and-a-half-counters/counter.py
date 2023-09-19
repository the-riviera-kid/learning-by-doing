class Counter:
    def __init__(self) -> None:
        self.result = 0

    def add(self) -> int:
        self.result += 1
        return self.result

    def total(self) -> int:
        return self.result
    
    def reset(self) -> int:
        self.result = 0
        return self.result

# CARLA BOUNDARY
# Fill in the blanks in the Counter class to make
# the following code work. You are *not* allowed
# to change any code under the Carla Boundary.
# -----------------------------------------------


# add() -> add 2 numbers together (one of the numbers is always 1)
# total() -> presents the total
# reset() -> sets the total to zero

pies_eaten = Counter()
pies_eaten.add()
pies_eaten.add()
# You have eaten 2 pies
print(f'You have eaten {pies_eaten.total()} pies')
pies_eaten.add()
# You have eaten 3 pies
print(f'You have eaten {pies_eaten.total()} pies')

days_since_accident = Counter()
# It has been 0 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')
for i in range(10):
    days_since_accident.add()
# It has been 10 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')
# Goddamnit, Irene
print('Oh no! Due to Irene running in a no running zone, Colin has lost both legs!')
days_since_accident.reset()
# It has been 0 days since an accident
print(f'It has been {days_since_accident.total()} days since an accident')

pies_eaten.add()
# You have eaten 4 pies
print(f'You have eaten {pies_eaten.total()} pies')


