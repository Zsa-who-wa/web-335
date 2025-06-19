"""
Author: Wendy Rzechula
Date: 6/19/2025
File Name: Rzechula_lemonadeStand.py
Description: Python program that simulates a lemonade stand.
Github Link: https://github.com/Zsa-who-wa/web-335.git
"""

# Calculates the cost of making lemonade (lemons and sugar).
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost

# Calculates the profit from selling lemonade.
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    profit = selling_price - (lemons_cost + sugar_cost)
    return profit

# Defines the cost of lemons, sugar and the selling price.
lemons_cost = 3.50
sugar_cost = 2.00
selling_price = 7.00

# Calculates total cost.
total_cost = calculate_cost(lemons_cost, sugar_cost)
cost_output = f"${lemons_cost:.2f} + ${sugar_cost:.2f} = ${total_cost:.2f}"
print("Cost Calculation:", cost_output)

# Calculates and outputs the profit calculation.
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)
profit_output = f"Selling price: ${selling_price:.2f} - Cost: ${total_cost:.2f} = Profit: ${profit:.2f}"
print("Total Profit: ", profit_output)

"""
SOURCES:
[Professor Darrell]. (2020, May 20). Function Returns [Video]. Bellevue University. 
https://bellevue.mediaspace.kaltura.com/media/Function+Returns/1_3w0ut032

[Professor Darrell]. (2020, May 20). String Variables and String Outputs [Video]. Bellevue University. 
https://bellevue.mediaspace.kaltura.com/media/String+Variables+and+String+Outputs/1_bd44wtd0

PFB Staff Writer (2023, June 30). Python String Concatenation and Formatting. Retrieved June 19, 2025, from 
https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python

[Programming With Mosh]. (2020, September 16). Python for Beginners - Learn Coding with Python in 1 Hour [Video]. 
YouTube. https://www.youtube.com/watch?v=kqtD5dpn9C8&t=361s

GeeksforGeeks (2024, April 24). How to format numbers as currency strings in Python. 
Retrieved June 19, 2025, from https://www.geeksforgeeks.org/how-to-format-numbers-as-currency-strings-in-python/
"""