/**
 * Title: Rzechula_MongoDB_Shell.js
 * Author: Wendy Rzechula
 * Date: June 22, 2025
 * Description: MongoDB Shell Queries for the users collection.
*/

// Displays all users in the collection
db.users.find()

// Displays the user with the email address jbach@me.com
db.users.findOne({ email: "jbach@me.com"});

// Displays the user with the last name Mozart
db.users.findOne({lastName: "Mozart" });

// Displays the user with the first name Richard
db.users.findOne({lastName: "Richard" });

// Displays the user with the employee ID 1010
db.users.findOne({ employeeid: "1010" });

/**
 * SOURCES
 * MongoDB: The Definitive Guide (Third Edition) 
 * Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020
*/