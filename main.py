# Imports
import argparse
import csv
from datetime import datetime, date, timedelta
from prettytable import PrettyTable

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# Main function
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Supermarket CLI')

    # Create subparsers
    subparsers = parser.add_subparsers(dest='command')

    # Create a parser for the "buy" command
    buy_parser = subparsers.add_parser('buy', help='Buy a new product')
    buy_parser.add_argument('name', help='Product name')
    buy_parser.add_argument('price', type=float, help='Product price')
    buy_parser.add_argument('quantity', type=int, help='Product quantity')
    buy_parser.add_argument('expiration', help='Product expiration date')

    # Create a parser for the "sell" command
    sell_parser = subparsers.add_parser('sell', help='Sell a product')
    sell_parser.add_argument('name', help='Product name')
    sell_parser.add_argument('sell_price', type=float, help='Selling price')

    # Create a parser for the "list" command
    list_parser = subparsers.add_parser('list', help='List all products')

    # Create a parser for the "forward" command
    forward_parser = subparsers.add_parser('forward', help='Travel forward in time')
    forward_parser.add_argument('days', type=int, help='Number of days to travel forward')

    # Create a parser for the "backward" command
    backward_parser = subparsers.add_parser('backward', help='Travel backward in time')
    backward_parser.add_argument('days', type=int, help='Number of days to travel backward')

    # Create a parser for the "profit" command
    profit_parser = subparsers.add_parser('profit', help='Calculate profit for a specific date')
    profit_parser.add_argument('date', help='The date to calculate profit for (format: YYYY-MM-DD)')

    # Parse the arguments
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command == 'buy':
        buy_product(args.name, args.price, args.quantity, args.expiration)
    elif args.command == 'sell':
        sell_product(args.name, args.sell_price)
    elif args.command == 'list':
        list_products()
    elif args.command == 'forward':
        time_machine.travel_forward(days=args.days)
        print(f"Traveled forward in time by {args.days} day(s). Current time: {time_machine.get_current_time()}")
    elif args.command == 'backward':
        time_machine.travel_backward(days=args.days)
        print(f"Traveled backward in time by {args.days} day(s). Current time: {time_machine.get_current_time()}")
    elif args.command == 'profit':
        print(f"Total profit: {calculate_profit(args.date)}")
    # If no arguments are passed, print the help message
    else:
        parser.print_help()

# TimeMachine class
class TimeMachine:
    # Constructor
    def __init__(self):
        self.current_time = datetime.now()
    # Method to get the current time
    def get_current_time(self):
        return self.current_time
    # Method to set the current time
    def travel_forward(self, days=0, hours=0, minutes=0, seconds=0):
        self.current_time += timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    # Method to set the current time
    def travel_backward(self, days=0, hours=0, minutes=0, seconds=0):
        self.current_time -= timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
# Create a TimeMachine instance
time_machine = TimeMachine()

# Function to add a bought product to a CSV file
def add_bought_to_csv(product_name, price, quantity, expiration_date, filename='bought.csv', bought_date_str=None):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the product details as a new row in the CSV file
        writer.writerow([product_name, price, quantity, expiration_date, bought_date_str])
    # Print a confirmation message
    print(f'Bought product: {product_name} with price: {price} and quantity: {quantity} and expiration date: {expiration_date}')

# Function to add a sold product to a CSV file
def add_sold_to_csv(product_name, price, quantity, expiration_date, filename='sold.csv', sell_price=None, sold_date_str=None):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the product details as a new row in the CSV file
        writer.writerow([product_name, price, quantity, expiration_date, sell_price, sold_date_str])
    # Print a confirmation message
    print(f'Sold product: {product_name} with sell price: {sell_price} and sold date: {sold_date_str}')

# Function to buy a product
def buy_product(product_name, price, quantity, expiration_date, filename='bought.csv', bought_date=None):
    # If no date is provided, use the current date
    if not bought_date:
        bought_date = time_machine.get_current_time()
    # Add the product to the 'bought.csv' file
    bought_date_str = bought_date.strftime('%Y-%m-%d')
    add_bought_to_csv(product_name, price, quantity, expiration_date, filename, bought_date_str)

# Function to sell a product
def sell_product(product_name, sell_price, sold_date=None, filename='sold.csv'):
    # If no date is provided, use the current date
    if not sold_date:
        sold_date = time_machine.get_current_time()
    # Get the product details
    product = get_product_details(product_name)
    if product:
        price, quantity, expiration_date, bought_date= product
        # Add the product to the 'sold.csv' file
        sold_date_str = sold_date.strftime('%Y-%m-%d')
        add_sold_to_csv(product_name, price, quantity, expiration_date, filename, sell_price, sold_date_str)
        # Remove the product from the 'bought.csv' file
        remove_from_csv(product_name, 'bought.csv')
    else:
        # Print an error message if the product is not found
        print(f"Error: Product '{product_name}' is out of stock.")

# Function to remove a product from a CSV file
def remove_from_csv(product_name, filename):
    # Open the CSV file in read mode
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Read the products into a list
        products = list(reader)

    # Filter out the product to be removed
    products = [product for product in products if product[0] != product_name]

    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write each product to the CSV file
        for product in products:
            writer.writerow(product)
        
# Function to get the details of a product
def get_product_details(product_name):
    # Open the 'bought.csv' file in read mode
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        # Read the products into a list
        products = list(reader)
        # Find the product with the given name
        for product in products:
            if product[0] == product_name:
                # Return the details of the product
                return product[1:]
    # If the product is not found, return None
    return None
    
# Function to list the products
def list_products(print_table=True):
    # Open the CSV file in read mode
    with open('bought.csv', 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        # Read the products into a list
        products = list(reader)
        # If the print_table argument is True, print the table
        if print_table:
            # Create a table with column names
            table = PrettyTable(['Product Name', 'Price', 'Quantity', 'Expiration Date', 'Bought Date'])
            # For each product in the list
            for product in products:
                # If the product has the correct number of columns
                if len(product) == 5:
                    # Convert each element to a string and strip whitespace
                    product = [str(element).strip() for element in product]
                    # Add the product as a row in the table
                    table.add_row(product)
                else:
                    # If the product does not have the correct number of columns, print a warning message
                    print(f"Skipping product {product} because it has {len(product)} columns instead of 5.")
            # Print the table
            print(table)
    # Return the list of products
    return products

def calculate_profit(date):
    # Initialize the total profit to 0
    total_profit = 0.0

    # Convert the date from string to date object
    date = datetime.strptime(date, '%Y-%m-%d').date()

    # Open the 'sold.csv' file in read mode
    with open('sold.csv', 'r') as sold_file:
        # Create a CSV reader
        sold_reader = csv.reader(sold_file)
        # Read the sold products into a list
        sold_products = list(sold_reader)

    # For each sold product
    for sold_product in sold_products:
        # Check if the product was sold on or before the given date
        if datetime.strptime(sold_product[5], '%Y-%m-%d').date() <= date:
            # Get the buy price and sell price from the sold product
            buy_price = float(sold_product[1])
            sell_price = float(sold_product[4])
            # Calculate the profit for this product
            profit = sell_price - buy_price
            # Add the profit to the total profit
            total_profit += profit

    # Return the total profit
    return total_profit

if __name__ == "__main__":
    main()