# Imports
import argparse
import csv
from datetime import datetime, timedelta
import time
import os
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

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
    profit_parser.add_argument('date', help='The date to calculate profit for (format: YYYY-MM-DD, "today", or "yesterday")')

    # Create a parser for the "revenue" command
    revenue_parser = subparsers.add_parser('revenue', help='Calculate revenue for a specific date')
    revenue_parser.add_argument('date', help='The date to calculate revenue for (format: YYYY-MM-DD, "today", or "yesterday")')
    
    # Create a parser for the "reset" command
    reset_parser = subparsers.add_parser('reset_date', help='Reset the date')

    # Parse the arguments
    args = parser.parse_args()
    
    # Create a console object
    console= Console()

 # Call the appropriate function based on the command
    if args.command == 'buy':
        # Create a progress bar
        progress = Progress()
        with progress:
            task = progress.add_task("[cyan]Buying...", total=100)
            while not progress.finished:
                progress.update(task, advance=10)
                time.sleep(0.2)
        buy_product(args.name, args.price, args.quantity, args.expiration)
        # Print a message to confirm the purchase
        console.print(f"Bought {args.quantity} {args.name}(s) with price {args.price} each and expiration date {args.expiration}.", style="bold blue")
    elif args.command == 'sell':
        # Create a progress bar
        progress = Progress()
        with progress:
            task = progress.add_task("[cyan]Selling...", total=100)
            while not progress.finished:
                progress.update(task, advance=10)
                time.sleep(0.2)
        sell_product(args.name, args.sell_price)
        # Print a message to confirm the sale
        console.print(f"Sold {args.name} for {args.sell_price}.", style="bold blue")
    elif args.command == 'list':
        list_products()
    elif args.command == 'forward':
        time_machine.travel_forward(days=args.days)
        # Print a message to confirm the time travel
        console.print(f"Traveled forward in time by {args.days} day(s). Current time: {time_machine.get_current_time()}", style="bold green")
    elif args.command == 'backward':
        time_machine.travel_backward(days=args.days)
        # Print a message to confirm the time travel
        console.print(f"Traveled backward in time by {args.days} day(s). Current time: {time_machine.get_current_time()}", style="bold red")
    elif args.command == 'profit':
        # Calculate the profit for the specified date
        console.print(f"The total profit on {args.date} is: {calculate_profit(args.date)}", style="bold yellow")
    elif args.command == 'revenue':
        # Calculate the revenue for the specified date
        console.print(f"The total revenue on {args.date} is: {calculate_revenue(args.date)}", style="bold cyan")
    elif args.command == 'reset_date':
        time_machine.reset_date()
        # Print a message to confirm the date reset
        console.print(f"Reset the date to the current date: {time_machine.get_current_time()}", style="bold magenta")
    # If no arguments are passed, print the help message
    else:
        parser.print_help()

# TimeMachine class
class TimeMachine:
    # Constructor
    def __init__(self):
        if os.path.exists('date.txt') and os.stat('date.txt').st_size != 0:
            with open('date.txt', 'r') as file:
                self.current_date = file.read().strip()
        else:
            self.current_date = datetime.today().strftime('%Y-%m-%d')

    # Method to travel forward in time
    def travel_forward(self, days):
        self.current_date = (datetime.strptime(self.current_date, '%Y-%m-%d') + timedelta(days=days)).strftime('%Y-%m-%d')
        self._save_date()

    # Method to travel backward in time
    def travel_backward(self, days):
        self.current_date = (datetime.strptime(self.current_date, '%Y-%m-%d') - timedelta(days=days)).strftime('%Y-%m-%d')
        self._save_date()
    
    # Method to reset the date to the current date
    def reset_date(self):
        self.current_date = datetime.today().strftime('%Y-%m-%d')
        self._save_date()

    # Method to get the current time
    def get_current_time(self):
        return self.current_date

    # Private method to save the current date to a file
    def _save_date(self):
        with open('date.txt', 'w') as file:
            file.write(self.current_date)

# Create a TimeMachine instance
time_machine = TimeMachine()

# Function to add a bought product to a CSV file
def add_bought_to_csv(product_name, price, quantity, expiration_date, filename='bought.csv', bought_date_str=None):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the product details as a new row in the CSV file
        writer.writerow([product_name, price, quantity, expiration_date, bought_date_str])

# Function to add a sold product to a CSV file
def add_sold_to_csv(product_name, price, quantity, expiration_date, filename='sold.csv', sell_price=None, sold_date_str=None):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the product details as a new row in the CSV file
        writer.writerow([product_name, price, quantity, expiration_date, sell_price, sold_date_str])

# Function to buy a product
def buy_product(product_name, price, quantity, expiration_date, filename='bought.csv', bought_date=None):
    # If no date is provided, use the current date
    if not bought_date or bought_date.lower() == 'today':
        bought_date = time_machine.get_current_time()
    elif bought_date.lower() == 'yesterday':
        bought_date = (datetime.strptime(time_machine.get_current_time(), '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    # Add the product to the 'bought.csv' file
    add_bought_to_csv(product_name, price, quantity, expiration_date, filename, bought_date)

# Function to sell a product
def sell_product(product_name, sell_price, sold_date=None, filename='sold.csv'):
    # If no date is provided, use the current date
    if not sold_date or sold_date.lower() == 'today':
        sold_date = time_machine.get_current_time()
    elif sold_date.lower() == 'yesterday':
        sold_date = (datetime.strptime(time_machine.get_current_time(), '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    # Get the product details
    product = get_product_details(product_name)
    if product:
        price, quantity, expiration_date, bought_date= product
        # Add the product to the 'sold.csv' file
        add_sold_to_csv(product_name, price, quantity, expiration_date, filename, sell_price, sold_date)
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

        # Create a console object
        console = Console()

        # Create a table
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Product Name")
        table.add_column("Price")
        table.add_column("Quantity")
        table.add_column("Expiration Date")
        table.add_column("Bought Date")

        # Convert each element to a string and strip whitespace
        for product in products:
            if len(product) == 5:
                product = [str(element).strip() for element in product]
                # Add the product as a row in the table
                table.add_row(*product)
            else:
                # If the product does not have the correct number of columns, print a warning message
                console.print(f"Skipping product {product} because it has {len(product)} columns instead of 5.")
        # If the print_table argument is True, print the table
        if print_table:
            console.print(table)
    # Return the list of products
    return products

def calculate_profit(date='today'):
    # If 'today' is specified, use the TimeMachine's current date
    if date.lower() == 'today':
        date = time_machine.get_current_time()
    elif date.lower() == 'yesterday':
        date = (datetime.strptime(time_machine.get_current_time(), '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        # If a specific date is specified, parse the date string into a date object
        date = datetime.strptime(date, '%Y-%m-%d').date()
    
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

def calculate_revenue(date='today'):
    # If 'today' is specified, use the TimeMachine's current date
    if date.lower() == 'today':
        date = time_machine.get_current_time()
    elif date.lower() == 'yesterday':
        date = (datetime.strptime(time_machine.get_current_time(), '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        # If a specific date is specified, parse the date string into a date object
        date = datetime.strptime(date, '%Y-%m-%d').date()
    
    # Initialize the total revenue to 0
    total_revenue = 0.0

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
            # Get the sell price from the sold product
            sell_price = float(sold_product[4])
            # Add the sell price to the total revenue
            total_revenue += sell_price

    # Return the total revenue
    return total_revenue

if __name__ == "__main__":
    main()