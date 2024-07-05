# POSHAAK Database System using SQL and Python
https://drive.google.com/file/d/1pX8DtPOJobOOzKzeSrjdoy545wmHssM5/view?usp=sharing
POSHAAK is a database management system built using PyQt6 for the interface of an online store that specializes in children's clothing. This project was developed as part of a university final project in database management.

## Description

The POSHAAK system provides a user-friendly interface for managing an online store's inventory, customers, and administrative tasks. The application supports two types of users: administrators and customers. Each user type has distinct interfaces and functionalities tailored to their roles.

### Key Features

- **User Management**: Separate interfaces for administrators and customers.
- **Product Management**: Add, update, and delete products in the inventory.
- **Customer Management**: Manage customer information and view order history.
- **Order Processing**: Facilitate order placement and tracking.
- **Database Integration**: Built on SQL for robust data management.

## Installation

To run this project on your local desktop, follow these steps:

### Step 1: Create Database

1. Set up a new database named `POSHAAK`.
2. Use the SQL script provided in the `database` folder to create the necessary tables.

### Step 2: Install Dependencies

Ensure you have Python installed on your system. Install required Python packages using pip:

```sh
pip install pyqt6 pyqt5
Step 3: Run the Application
Execute the main Python script to launch the application:
```
```sh
Copy code
python main.py
Usage
Login
Administrators and customers can log in using credentials stored in the customers table.
Administrators have a user type marked as 'star' in the customers table.
Interface
The application uses .ui files for the graphical interface, leveraging both PyQt5 and PyQt6.
Functionality
Admins: Manage products, view all customer orders, and update customer information. The delete functionality for admins can be further expanded.
Customers: Browse products, place orders, and view personal order history.
Screenshots
(Add screenshots here)

Explanation of the Project
This project has two types of users: admins and customers, each with different interfaces. Admins have a user type marked as 'star' in the customers table. Feel free to log in with credentials from the customer table. The screens are .ui files, and the code uses both PyQt5 and PyQt6 in some places. The delete functionality can be expanded more for the admin.

Contributing
We welcome contributions! Please fork the repository and submit a pull request.
