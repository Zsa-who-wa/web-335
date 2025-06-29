/**
 * Title: Rzechula_Assignment_5_2_Projections.js
 * Author: Wendy Rzechula
 * Date: June 29, 2025
 * Description: MongoDB Document Manipulation and Projections.
*/

// Pulled up all users to see data information
db.users.find()

// Add new user to the user’s collection
db.users.insertOne({
  firstName: 'Wendy',
  lastName: 'Rzechula',
  email: 'wrzechula@me.com',
  employeeId: '1013',
  dateCreated: new Date()
})

// Update Mozart’s email address to mozart@me.com
db.users.updateOne({employeeId: '1009'}, {$set: {email: 'mozart@me.com'}});

// prove the document was updated successfully
db.users.findOne({employeeId: '1009'});

// Display all users in the collection using projections to only show the first name, last name, and email address.
db.users.find({}, { firstName: 1, lastName: 1, email: 1 });

/**
 * SOURCES
 * MongoDB: The Definitive Guide (Third Edition) 
 * Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020
*/