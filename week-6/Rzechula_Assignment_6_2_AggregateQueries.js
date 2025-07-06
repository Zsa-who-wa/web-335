/**
 * Title: Rzechula_Assignment_6_2_AggregateQueries.js
 * Author: Wendy Rzechula
 * Date: July 5, 2025
 * Description: Assignment 6.2 - Aggregate Queries
*/

// a. Display all students
db.students.find()

// b. Add a new student
db.students.insertOne({
  firstName: 'Hermione',
  lastName: 'Weasley',
  studentId: 's2424',
  houseId: 'h1008'
})

// Verify new student was added
db.students.find({ studentId: 's2424' });

// c. Update property of new student's last name
db.students.updateOne(
  { studentId: 's2424' }, 
  {$set: { lastName: 'Granger' } }
);

// Verify new student's last name was updated successfully
db.students.find({ studentId: 's2424' });

// d. Delete new student that was just added
db.students.deleteOne({ studentId: 's2424' });

// Verify new student was deleted
db.students.find({ studentId: 's2424' });

// e. Display all students by house
db.houses.aggregate([
  {
    $lookup: {
      from: 'students', 
      localField: 'houseId',
      foreignField: 'houseId',
      as: 'students'
    }
  },
  {
    $project: {
      _id: 0,
      house: "$houseId",
      mascot: 1,
      founder: 1,
      students: 1
    } 
  }
]);

// f. Display all students in Gryffindor house
db.houses.aggregate([
  { $match: { houseId: 'h1007' } },
  {
    $lookup: {
      from: 'students',
      localField: 'houseId',
      foreignField: 'houseId',
      as: 'students'
    }
  },
  {
    $project: {
      _id: 0,
      house: "$houseId",
      mascot: 1,
      founder: 1,
      students: 1
    }
  }
]);

// g. Display all students in house with Eagle Mascot
db.houses.aggregate([
  { $match: { mascot: 'Eagle' } },
  {
    $lookup: { 
      from: 'students',
      localField: 'houseId',
      foreignField: 'houseId',
      as: 'students' 
    }
  },
  {
    $project: {
      _id:0,
      house: "$houseId",
      mascot: 1,
      founder: 1,
      students: 1
    }
  }
]);


/**
 * SOURCES
 * MongoDB: The Definitive Guide (Third Edition) 
 * Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020
*/