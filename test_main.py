import unittest
import csv
from io import StringIO
from datetime import date, datetime, timedelta
from contextlib import redirect_stdout
from main import buy_product, sell_product, list_products, TimeMachine

class TestMain(unittest.TestCase):
    def setUp(self):
        self.time_machine = TimeMachine()

    def test_buy_product(self):
        # Test buying a product
        buy_product('Apple', 1.0, 10, '2022-12-31')
        # Open the 'bought.csv' file and check if the product details are correct
        with open('bought.csv', 'r') as file:
            last_line = list(csv.reader(file))[-1]
            self.assertEqual(last_line, ['Apple', '1.0', '10', '2022-12-31', date.today().strftime('%Y-%m-%d')])

    def test_sell_product(self):
        # Test selling a product
        sell_product('Apple', 0.5)
        # Open the 'sold.csv' file and check if the product details are correct
        with open('sold.csv', 'r') as file:
            last_line = list(csv.reader(file))[-1]
            self.assertEqual(last_line, ['Apple', '1.0', '10', '2022-12-31', '0.5', date.today().strftime('%Y-%m-%d')])

    def test_list_products(self):
        # Test listing the products
        # Redirect the stdout to a string buffer
        f = StringIO()
        with redirect_stdout(f):
            list_products()
        # Get the output string
        output = f.getvalue()

    def test_travel_forward(self):
        current_time = self.time_machine.get_current_time()
        self.time_machine.travel_forward(days=1)
        expected_time = current_time + timedelta(days=1)
        self.assertEqual(self.time_machine.get_current_time(), expected_time)

    def test_travel_backward(self):
        current_time = self.time_machine.get_current_time()
        self.time_machine.travel_backward(days=1)
        expected_time = current_time - timedelta(days=1)
        self.assertEqual(self.time_machine.get_current_time(), expected_time)

if __name__ == '__main__':
    unittest.main()