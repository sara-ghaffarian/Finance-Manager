# Finance-Manager

#### Video Demo:

[https://youtube.com/shorts/LrwPpj6t5xM?feature=share]

## Description

Finance Manager is a command-line application written in Python that helps users manage their personal finances. The program allows users to record income and expense transactions, calculate their balance, search transactions by category, and save financial data for future use.

This project was developed as my CS50 Final Project and combines several concepts learned throughout the course, including object-oriented programming, file handling, exception handling, data validation, JSON storage, and automated testing with pytest.

## Features

The application provides the following features:

* Add income transactions
* Add expense transactions
* Delete existing transactions
* View all saved transactions
* Calculate current balance
* Calculate total income
* Calculate total expenses
* Find the category with the highest expenses
* Search transactions by category
* Save data to a JSON file
* Load saved data automatically when the program starts

## Project Files

### project.py

This file contains the main application logic.

The project is built around two classes:

#### Transaction

Represents a single transaction and stores:

* Amount
* Category
* Transaction type (income or expense)

#### FinanceManager

Manages all transactions and provides methods for:

* Adding transactions
* Deleting transactions
* Calculating balance
* Calculating income and expenses
* Searching transactions
* Saving data
* Loading data

### test_project.py

Contains automated tests written with pytest.

The tests verify:

* Adding transactions
* Deleting transactions
* Balance calculation
* Income calculation
* Expense calculation
* Category searching
* Top expense category detection
* Validation functions

### transactions.json

Stores all transaction data in JSON format so that information remains available between program executions.

## Validation

The application validates user input before adding transactions.

Rules include:

* Transaction amount must be greater than zero.
* Transaction type must be either "income" or "expense".

Invalid data causes the program to raise appropriate exceptions.

## Design Choices

I decided to use object-oriented programming because it makes the project easier to organize and maintain. Separating the Transaction and FinanceManager classes helped keep transaction data separate from the business logic.

I chose JSON for data storage because it is simple, human-readable, and supported directly by Python without additional libraries.

The project uses a command-line interface to focus on Python programming concepts rather than web development.

## Future Improvements

Possible future improvements include:

* Monthly financial reports
* Expense filtering by date
* Budget planning tools
* Data visualization and charts
* Exporting reports to CSV files

## Conclusion

Finance Manager is a practical application that helps users track their finances while demonstrating many of the programming concepts covered in CS50. The project combines data management, validation, file storage, testing, and object-oriented design into a complete and functional program.
