"""
Author: Wendy Rzechula
Date: 7/11/2025
File Name: Rzechula_usersp2.py
Description: Python program that connects web335DB and performs various CRUD operations
Github Link: https://github.com/Zsa-who-wa/web-335.git
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime
from pprint import pprint

# 2. Connect to MongoDB web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.jhzzmwd.mongodb.net/web335DB?retryWrites=true&w=majority")

# Confirm successful connection to web335DB
print("Connected to MongoDB:", client)

# Access the web335DB database
db = client['web335DB']

# 3. Creates a new user document
my_user = {
    "firstName": "Ryesha",
    "lastName": "Reed",
    "employeeId": "1111",
    "email": "rreed@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the new document into the users collection
user_id = db.users.insert_one(my_user).inserted_id
print("INSERT NEW DOCUMENT", user_id)

# 4. Prove document was created
print("DOCUMENT WAS INSERTED: ")
pprint(db.users.find_one({"employeeId": "1111"}))

# 5. Update the users email address created in step 3
db.users.update_one(
    {"employeeId": "1111"},
    {"$set":{"email": "ryeshareed@me.com"}}
)

# 6. Prove document was updated
print("DOCUMENT WAS UPDATED: ")
pprint(db.users.find_one({"employeeId": "1111"}))

# 7. Delete the document that was created in step 3
result = db.users.delete_one({"employeeId": "1111"})

# 8. Prove the document was deleted
print(result)
print("DOCUMENT WAS DELETED: ")
pprint(db.users.find_one({"employeeId": "1111"}))



"""
SOURCES:
MongoDB: The Definitive Guide (Third Edition) 
Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020

Currie, I. (n.d.). Prettify Your Data Structures With Pretty Print in Python. 
Retrieved July 6, 2025, from https://realpython.com/python-pretty-print/
"""