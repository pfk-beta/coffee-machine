from collections import namedtuple, defaultdict
from datetime import datetime
from time import sleep

from tqdm import tqdm

from exceptions import TooMuchWaterException, TooMuchCoffeeException, MaitenanceException, NoWaterException, \
    NoCoffeeBeansException, NoMilkException

Coffee = namedtuple(
    'Coffee',
    ['name', 'size', 'water', 'coffee_beans', 'milk'])


class CoffeeMachine:
    WATERTANK_SIZE = 5000
    COFFEETANK_SIZE = 1000
    NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES = 2000  # every 2000 coffees, machine should call for
    TIME_OF_PREPARING_COFFEE = 100 * 0.05

    COFFEE_DEFINITIONS = {
        'americano': Coffee('Americano', 200, 200, 30, 0),
        'capuchino': Coffee('Capuchino', 200, 170, 30, 30),
        'espresso': Coffee('Espresso', 50, 50, 30, 0),
        'late_machiato': Coffee('Late Machiato', 200, 200, 30, 30),
    }

    def __init__(self, water_level, coffeebeans_level):
        self.__watertank_level = min(water_level, CoffeeMachine.WATERTANK_SIZE)
        self.__coffeebeans_level = min(coffeebeans_level, CoffeeMachine.COFFEETANK_SIZE)
        self.__milk_level = 0
        self.__coffee_counter = 0
        self.__coffee_start = datetime.now()
        self.__coffee_stats = defaultdict(int)

    def fill_water(self, water_amount=500):
        if self.__watertank_level + water_amount > CoffeeMachine.WATERTANK_SIZE:
            raise TooMuchWaterException()
        self.__watertank_level += water_amount

    def fill_coffee(self, coffeebeans_level_amount=200):
        if self.__coffeebeans_level + coffeebeans_level_amount > CoffeeMachine.COFFEETANK_SIZE:
            raise TooMuchCoffeeException()
        self.__coffeebeans_level += coffeebeans_level_amount

    def attach_milkbox(self, milkbox=1000):
        self.__milk_level = milkbox

    def get_americano(self):
        return self.__get_coffee('americano')

    def get_espresso(self):
        return self.__get_coffee('espresso')

    def get_capuchino(self):
        return self.__get_coffee('capuchino')

    def get_late_machiato(self):
        return self.__get_coffee('late_machiato')

    def showme_coffee_stats(self):
        print(self.__coffee_stats)

    def showme_uptime(self):
        delta = datetime.now() - self.__coffee_start
        print("%d seconds" % delta.seconds)

    def __get_coffee(self, coffee_type):
        if self.__coffee_counter == CoffeeMachine.NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES:
            raise MaitenanceException()

        coffee = CoffeeMachine.COFFEE_DEFINITIONS[coffee_type]

        if coffee.water > self.__watertank_level:
            raise NoWaterException()

        if coffee.coffee_beans > self.__coffeebeans_level:
            raise NoCoffeeBeansException()

        if coffee.milk > self.__milk_level:
            raise NoMilkException()

        return self.__prepare_coffee(coffee)

    def __prepare_coffee(self, coffee):
        self.__coffeebeans_level -= coffee.coffee_beans
        self.__watertank_level -= coffee.water
        self.__milk_level -= coffee.milk

        for x in tqdm(range(100)):
            # TODO: more spectacular, progressbar of emptying tanks
            sleep(CoffeeMachine.TIME_OF_PREPARING_COFFEE / 100.)

        self.__coffee_counter += 1
        self.__coffee_stats[coffee.name] += 1

        return coffee
