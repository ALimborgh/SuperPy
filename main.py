# Imports
import argparse
import csv
from datetime import date
from datetime import datetime
from prettytable import PrettyTable

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# Main function
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Supermarket CLI')

    # Add arguments to the parser
    parser.add_argument('-b', '--buy', nargs=4, metavar=('name', 'price', 'quantity', 'expiration'), help='Buy a new product')
    parser.add_argument('-s', '--sell', nargs=2, metavar=('name', 'sell-price'), help='Sell a product')
    parser.add_argument('-l', '--list', action='store_true', help='List all products')

    # Parse the arguments
    args = parser.parse_args()

    # If the buy argument is passed, unpack the values and call the buy_product function
    if args.buy:
        name, price, quantity, expiration = args.buy
        buy_product(name, price, quantity, expiration)
    # If the sell argument is passed, call the sell_product function
    elif args.sell:
        name, sell_price = args.sell
        sell_product(name, sell_price)
    # If the list argument is passed, call the list_products function
    elif args.list:
        list_products()
    # If no arguments are passed, print the help message
    else:
        parser.print_help()

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
        bought_date = date.today()
    # Add the product to the 'bought.csv' file
    bought_date_str = bought_date.strftime('%Y-%m-%d')
    add_bought_to_csv(product_name, price, quantity, expiration_date, filename, bought_date_str)

# Function to sell a product
def sell_product(product_name, sell_price, sold_date=None, filename='sold.csv'):
    # If no date is provided, use the current date
    if not sold_date:
        sold_date = date.today()
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

if __name__ == "__main__":
    main()