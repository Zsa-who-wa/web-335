"""
Author: Wendy Rzechula
Date: 6/27/2025
File Name: Rzechula_lemonadeStand.py
Description: Python program that manages a weekly schedule for a lemonade stand
Github Link: https://github.com/Zsa-who-wa/web-335.git
"""

# List of tasks for lemonade stand
tasks = ["Buy Lemons", "Make Lemonade", "Sell Lemonade", "Clean Up", "Deposit Cash"]

# FOR loop to print each task
for task in tasks:
    print("* " + task)

print () # prints blank line for spacing

# List of days of the week (Sunday - Saturday)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("WEEKLY SCHEDULE:")
# For loop with an if..else to assign tasks to days
for i in range(len(days)):
    day = days[i]
    if day == "Saturday" or day == "Sunday":
        print(day + ": DAY OFF. It's time to rest!") # Weekend message
    else:
        task = tasks[i % len(tasks)]
        print(day + ": " + task) #Prints task for each day

"""
SOURCES:
W3Schools (n.d.). Python Lists. Retrieved June 27, 2025, from https://www.w3schools.com/python/python_lists.asp
W3Schools (n.d.). Python - Loop Lists. Retrieved June 27, 2025, from https://www.w3schools.com/python/python_lists_loop.asp
W3Schools (n.d.). Python If ... Else. Retrieved June 27, 2025, from https://www.w3schools.com/python/python_conditions.asp
W3Schools (n.d.). Python Operators. Retrieved June 27, 2025, from https://www.w3schools.com/python/python_operators.asp
Hamedami, M. (n.d.). Python for Beginners - Learn Coding with Python in 1 Hour. Youtube. Retrieved June 27, 2025, from https://www.youtube.com/watch?v=kqtD5dpn9C8
"""