# Account Management GUI

A graphical interface built with Python's Tkinter library to create and manage bank accounts. This application allows users to add account information, validate inputs, and handle account types with different settings. Users can also import and export data in CSV format.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating Accounts](#creating-accounts)
  - [Managing Account Types](#managing-account-types)
  - [Importing and Exporting Data](#importing-and-exporting-data)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Account Creation**: Users can create new accounts by entering owner name, initial balance, and selecting the account type (Courant or Epargne).
- **Account Type Management**:
  - **Courant** accounts allow setting an overdraft limit.
  - **Epargne** accounts allow setting an interest rate.
- **Validation**: Ensures correct data input for account details.
- **Data Table**: Displays all created accounts in a table format.
- **CSV Import/Export**: Users can import account data from a CSV file or export current data to a CSV file.

## Technologies

- **Python**: Programming language used for the application logic.
- **Tkinter**: Standard Python library for creating the graphical interface.
- **CSV Module**: Used for importing and exporting data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/account-management-gui.git
   cd account-management-gui
