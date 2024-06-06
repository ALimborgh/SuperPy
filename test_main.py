import unittest
import csv
from io import StringIO
from datetime import date
from contextlib import redirect_stdout
from main import buy_product, sell_product, list_products

class TestMain(unittest.TestCase):
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
        # Open the 'bought.csv' file and check if the output matches the products
        with open('bought.csv', 'r') as file:
            reader = csv.reader(file)
            products = list(reader)
            for product in products:
                # Split the product details into a list
                product_details = product
                # Check if each detail is in the output
                for detail in product_details:
                    self.assertIn(detail.strip(), output)

if __name__ == '__main__':
    unittest.main()