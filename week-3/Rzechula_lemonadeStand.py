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