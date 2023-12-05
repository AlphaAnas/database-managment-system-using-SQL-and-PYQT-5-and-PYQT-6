# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import pyodbc
 # Replace these with your own database connection details
server = 'DESKTOP-6367D0S'
database = 'POSHAAK'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'anasking'  # Specify a password if not using Windows Authentication


# # Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

class CustomerInterface(QtWidgets.QMainWindow):
        def __init__(self):
            # Call the inherited classes __init__ method
                super(CustomerInterface, self).__init__() 
                
                uic.loadUi("signup_Form.ui",self)
                
                # self.userEmail =  self.findChild(QLineEdit, "email").text()
                # self.firstName =  self.findChild(QLineEdit, "firstname").text()
                # self.lastName =   self.findChild(QLineEdit, "lastname").text()
                # self.password_field = self.findChild(QLineEdit, "pass").text()
                # self.password = self.password_field
                # self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
                
                self.signupButton1 = self.findChild(QPushButton, "signupButton")
                print(self.signupButton1)  # Check if this prints the correct button
                self.signupButton1.clicked.connect(self.insertCustomer)
                self.cancel = self.findChild(QPushButton, "cancelButton")
                self.cancel.clicked.connect(self.close)
                    
            ## when the user enters their values insert a new user
        def insertCustomer(self):
                self.userEmail =  self.findChild(QLineEdit, "email").text()
                self.firstName =  self.findChild(QLineEdit, "firstname").text()
                self.lastName =   self.findChild(QLineEdit, "lastname").text()
                self.password_field = self.findChild(QLineEdit, "pass")
                self.password = self.password_field.text()
                self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
                connection = pyodbc.connect(
                        connection_string
                    )

                cursor = connection.cursor()
                print( self.userEmail,  self.password,  self.firstName,  self.lastName, "printed")
                cursor.execute("INSERT INTO customers values(?,?,?,?);" , ( self.lastName,  self.userEmail,  self.password, 'normal'))
                connection.commit()

                # Retrieve the newly inserted customer ID
                cursor.execute("select id, last_name from customers where id = (select max(id) from customers)")
                result = cursor.fetchone()
                customer_id = result[0]
                customer_name = result[1]
            


                # Show a message box with the customer ID
                connection.close()
                QtWidgets.QMessageBox.information(
                    self, "customer Inserted", f"Customer ID : {customer_id} , Customer Name :{customer_name} has been inserted successfully.")
        # if the user enters some wrong values 
    
        def close(self):
            self.hide()
            
            
        # Close the database connection
       
        #   # login function  
      
                
        

    


