import unittest
from coffeemachine import CoffeeMachine, NoWaterException, NoCoffeeBeansException, MaitenanceException


class TestCoffeeMachine(unittest.TestCase):

    def test_empty_watertank(self):
        coffeemachine = CoffeeMachine(0, 1000)
        with self.assertRaises(NoWaterException) as context:
            coffeemachine.get_americano()

    def test_empty_coffeetank(self):
        coffeemachine = CoffeeMachine(1000, 0)
        with self.assertRaises(NoCoffeeBeansException) as context:
            coffeemachine.get_americano()

    def test_empty_coffetank_and_watertank(self):

        coffeemachine = CoffeeMachine(0, 0)
        with self.assertRaises(NoWaterException) as context:
            coffeemachine.get_americano()

        coffeemachine.fill_water(1000)

        with self.assertRaises(NoCoffeeBeansException) as context:
            coffeemachine.get_americano()

        coffeemachine.fill_coffee(222)

        coffeemachine.get_americano()

    def test_almost_empty_coffeetank(self):
        coffeemachine = CoffeeMachine(1000, 29)

        with self.assertRaises(NoCoffeeBeansException) as context:
            coffeemachine.get_espresso()

        coffeemachine.fill_coffee(2)

        coffeemachine.get_americano()

    def test_maitenance_window(self):
        coffeemachine = CoffeeMachine(1000, 500)
        coffeemachine.coffee_counter = CoffeeMachine.NEED_TECHNICAL_SERVICE_AFTER_N_COFFEES

        # next coffee should cause problem with coffee machine

        with self.assertRaises(MaitenanceException) as context:
            coffeemachine.get_late_machiato()


if __name__ == '__main__':
    unittest.main()
