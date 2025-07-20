/**
 * Title: LogicLynx_Assignment_8_2_WhatABook_Queries.js
 * Author: John Kuronya, Wendy Rzechula, Christopher Weaver
 * Date: July 17, 2025
 * Description: Assignment 8.2 - WhatABook Database Modeling and Scripts
*/

// Display all books
db.books.find({}, { _id: 0, title: 1, author: 1, genre: 1 });

// Display a list of books by genre
db.books.find({genre: "Fantasy Fiction" }, { _id: 0, title: 1, author: 1 });

// Display a list of books by author
db.books.find({ "author.name": "Delia Owens" }, { _id: 0, title: 1, genre: 1 });

// Display all books
db.books.findOne({ bookId: "B1002" });


/**
 * SOURCES
 * MongoDB: The Definitive Guide (Third Edition) 
 * Shannon Bradshaw, Eoin Brazil, and Kristina Chodorow; O’Reilly; 2020
*/