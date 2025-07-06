"""
Author: Wendy Rzechula
Date: 7/6/2025
File Name: Rzechula_usersp1.py
Description: Python program that connects web335DB and performs various operations
Github Link: https://github.com/Zsa-who-wa/web-335.git
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime
from pprint import pprint

# Create a connection to MongoDB web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.jhzzmwd.mongodb.net/web335DB?retryWrites=true&w=majority")

# Confirm successful connection to web335DB
print("Connected to MongoDB:", client)

# Access the web335DB database
db = client['web335DB']

# Displays all users in the collection showing only first and last name
print("-------------")
print("ALL USERS (first and last name only):")
for user in db.users.find({}, {"firstName": 1, "lastName": 1 }):
    pprint(user)

# Find and print the document where the employee ID is 1011
print("-------------")
print("USER WITH employeeId 1011:")
pprint(db.users.find_one({"employeeId": "1011"}))

# Find and print the document where the last name is Mozart
print("-------------")
print("USER WITH LAST NAME 'Mozart':")
pprint(db.users.find_one({"lastName": "Mozart"}))



"""
SOURCES:
MongoDB: The Definitive Guide (Third Edition) 
Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020

Currie, I. (n.d.). Prettify Your Data Structures With Pretty Print in Python. 
Retrieved July 6, 2025, from https://realpython.com/python-pretty-print/
"""