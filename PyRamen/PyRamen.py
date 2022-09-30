# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter.
CURRENTLY HAVING TROUBLE ON LINE 84 - 115
TROUBLE CONVERTING THE PRICE TO AN INT
ALSO FAILING TO PICK UP ON COST ON LINE 97
"""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        # print(line)
        menu.append(line)

# print(menu)





# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        # print(line)
        sales.append(line)

# print(sales)





# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale_row in sales:



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    Line_Item_ID = sale_row[0]
    Date = sale_row[1]
    Credit_Card_Number = sale_row[2]
    Quantity = sale_row[3]
    Menu_Item = sale_row[4]


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if Menu_Item not in report:
        report[Menu_Item] = {
            '01-count': 0, 
            '02-revenue': 0, 
            '03-cogs': 0, 
            '04-profit': 0
        }









    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_row in menu:


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        Item = menu_row[0]
        Category = menu_row[1]
        Description = menu_row[2]
        Price = menu_row[3]
        print(f"this is the price: {Price}, type = {type(Price)}")
        # price_int_format = float(Price)
        # Cost = int(menu_row[4])

        print(Item)
        print(Category)
        print(Description)
        # print(f"price is: {Price}, cost is: {Cost}. Profit is: {Price - Cost}")
        # print(type(price_int_format))
        # print(Cost)                                                                                    )



        # @TODO: Calculate profit of each item in the menu data
        # proft = Price - Cost


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if Menu_Item == Item:

            # @TODO: Print out matching menu data
            # print(Item)
            print("")






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the sale_row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(row_count)



# @TODO: Write out report to a text file (won't appear on the command line output)
