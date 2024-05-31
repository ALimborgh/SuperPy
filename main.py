# Imports
import argparse
import csv
from datetime import date
from math import prod
import re
from prettytable import PrettyTable
import io

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    parser = argparse.ArgumentParser(description='Supermarket CLI')
    
    parser.add_argument('--add-product', nargs=2, metavar=('product_name', 'price'), help='Add a new product to the supermarket')
    parser.add_argument('--remove-product', metavar='product_name', help='Remove a product from the supermarket')
    parser.add_argument('--list-products', action='store_true', help='List all products in the supermarket')
    
    args = parser.parse_args()

    if args.add_product:
        product_name, price = args.add_product
        add_product(product_name, price)
    elif args.remove_product:
        remove_product(args.remove_product)
    elif args.list_products:
        list_products()
    else:
        parser.print_help()

#need fixing
def add_product(product_name, price):
    with open('products.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_name, price])
    print(f'Added product: {product_name} with price: {price}')

def remove_product(product_name):
    products = list_products(print_table=False)
    products = [product for product in products if product[0] != product_name]
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(products)  # Write the remaining products
    print(f'Successfully removed product: {product_name}')

def list_products(print_table=True):
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        products = list(reader)
        if print_table:
            table = PrettyTable(['Product Name', 'Price', 'Quantity', 'Expiration Date'])  # Set the column names
            for product in products:  # Add each product as a row
                if len(product) == 4:  # Check if product has the correct number of columns
                    product = [str(element).strip() for element in product]  # Convert each element to a string and strip whitespace
                    table.add_row(product)
                else:
                    print(f"Skipping product {product} because it has {len(product)} columns instead of 4.")
            print(table)
    return products
    
    


if __name__ == "__main__":
    main()