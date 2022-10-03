# -*- coding: UTF-8 -*-
"""PyRamen Homework - Complete"""


# Imports libraries used in reading files in the Resources director
import csv
from pathlib import Path


# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')


# Initialize list objects to hold our menu and sales data
menu = []
sales = []


# Reads in the menu data into the menu list
with open(menu_filepath, 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        menu.append(line)
# Removes the first item in menu
menu.pop(0)


# Reads in the sales data into the sales list
with open(sales_filepath, 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        sales.append(line)
# Removes the first item in sales
sales.pop(0)


# Initializes dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0


# Loops over every row in the sales list object
for sale_row in sales:

    # Initializes sales data variables
    Line_Item_ID = sale_row[0]
    Date = sale_row[1]
    Credit_Card_Number = sale_row[2]
    Quantity = int(sale_row[3])
    Menu_Item = sale_row[4]

    # If the item value not in the report, adds it as a new entry with initialized metrics
    if Menu_Item not in report and Menu_Item != "Menu_Item":
        report[Menu_Item] = {
            '01-count': 0, 
            '02-revenue': 0, 
            '03-cogs': 0, 
            '04-profit': 0
        }
    
    # @TODO: For every row in our sales data, Loops over the menu records to determine a match
    for menu_row in menu:
        # Initializes variable for the appropriate Menu_Item
        if Menu_Item == menu_row[0]:
            # is the next line "Item = menu_row[0]" needed ?
            Item = menu_row[0]
            # print(Item)
            Category = menu_row[1]
            Description = menu_row[2]
            Price = int(menu_row[3])
            Cost = int(menu_row[4])
            Profit = Price - Cost

            # Cumulatively adds the values to the corresponding metrics 
            report[Menu_Item]['01-count'] += Quantity
            report[Menu_Item]['02-revenue'] += Price * Quantity
            report[Menu_Item]['03-cogs'] += Cost * Quantity
            report[Menu_Item]['04-profit'] += Profit * Quantity

        # Passes/does nothing in case of no match
        else:
            pass
            
    # Increments the sale_row counter by 1
    row_count += 1


# Prints total number of records in sales data
print(f"Total records in sales data is: {row_count}.\nSee 'Results.txt' for full report.")


# Writes out report to a text file (won't appear on the command line output)
with open("Results.txt", "w") as file:
    for item in report:
    file.write(str(report))