from collections import namedtuple
from datetime import datetime


class NoMilkException(Exception):
    pass


class NoWaterException(Exception):
    pass


class NoCoffeeBeansException(Exception):
    pass


class MaitenanceException(Exception):
    pass


Coffee = namedtuple('Coffee', ['name', 'size', 'water', 'coffee_beans', 'milk'])


class CoffeeMachine:
    WATERTANK_SIZE = 5000
    COFFEETANK_SIZE = 1000
    NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES = 2000  # every 2000 coffees, machine should call for

    COFFEE_DEFINITIONS = {
        'americano': Coffee('Americano', 200, 200, 30, 0),
        'capuchino': Coffee('Capuchino', 200, 170, 30, 30),
        'espresso': Coffee('Espresso', 50, 50, 30, 0),
        'late_machiato': Coffee('Late Machiato', 200, 200, 30, 30),
    }

    def __init__(self, water_level, coffeebeans_level):
        self.watertank_level = min(water_level, CoffeeMachine.WATERTANK_SIZE)
        self.coffeebeans_level = min(coffeebeans_level, CoffeeMachine.COFFEETANK_SIZE)
        self.milk_level = 0
        self.coffee_counter = 0
        self.coffee_start = datetime.now()

    def fill_water(self, water_amount=500):
        self.watertank_level += water_amount

    def fill_coffee(self, coffeebeans_level_amount=200):
        self.coffeebeans_level += coffeebeans_level_amount

    def attach_milkbox(self, milkbox=1000):
        self.milk_level = milkbox

    def get_americano(self):
        return self._get_coffee('americano')

    def _get_coffee(self, coffee_type):
        if self.coffee_counter == CoffeeMachine.NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES:
            raise MaitenanceException()

        coffee = CoffeeMachine.COFFEE_DEFINITIONS[coffee_type]

        print("Prepare cup of size {} ml".format(coffee.size))

        if coffee.water > self.watertank_level:
            raise NoWaterException()

        if coffee.coffee_beans > self.coffeebeans_level:
            raise NoCoffeeBeansException()

        if coffee.milk > self.milk_level:
            raise NoMilkException()
