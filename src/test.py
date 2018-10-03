import unittest
from coffeemachine import CoffeeMachine
from exceptions import NoWaterException, NoCoffeeBeansException, MaitenanceException

class TestCoffeeMachine(unittest.TestCase):

    def test_empty_watertank(self):
        coffeemachine = CoffeeMachine(0, 1000)
        with self.assertRaises(NoWaterException) as context:
            coffee = coffeemachine.get_americano()
            self.assertIsNone(coffee)

    def test_empty_coffeetank(self):
        coffeemachine = CoffeeMachine(1000, 0)
        with self.assertRaises(NoCoffeeBeansException) as context:
            coffee = coffeemachine.get_americano()
            self.assertIsNone(coffee)

    def test_empty_coffetank_and_watertank(self):

        coffeemachine = CoffeeMachine(0, 0)
        with self.assertRaises(NoWaterException) as context:
            coffee = coffeemachine.get_americano()
            self.assertIsNone(coffee)

        coffeemachine.fill_water(1000)

        with self.assertRaises(NoCoffeeBeansException) as context:
            coffee = coffeemachine.get_americano()
            self.assertIsNone(coffee)

        coffeemachine.fill_coffee(222)

        coffee = coffeemachine.get_americano()
        self.assertEqual('Americano', coffee.name)

    def test_almost_empty_coffeetank(self):
        coffeemachine = CoffeeMachine(1000, 29)

        with self.assertRaises(NoCoffeeBeansException) as context:
            coffee = coffeemachine.get_espresso()
            self.assertIsNone(coffee)

        coffeemachine.fill_coffee(2)

        coffee = coffeemachine.get_americano()
        self.assertEqual('Americano', coffee.name)

    def test_maitenance_window(self):
        coffeemachine = CoffeeMachine(1000, 500)
        coffeemachine.coffee_counter = CoffeeMachine.NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES

        # next coffee should cause problem with coffee machine

        with self.assertRaises(MaitenanceException) as context:
            coffee = coffeemachine.get_late_machiato()
            self.assertIsNone(coffee)

    # TODO: test overflow tanks...


if __name__ == '__main__':
    unittest.main()
