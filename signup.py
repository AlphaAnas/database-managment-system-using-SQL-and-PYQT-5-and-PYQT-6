# Importing essential modules
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import re
import connection_string
import pyodbc
 # Replace these with your own database connection details
server = ''
database = 'POSHAAK'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = ''  # Specify a password if not using Windows Authentication


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
                
                
             
                self.pass1.setEchoMode(QLineEdit.EchoMode.Password)
                
             
               
                
                self.signupButton.clicked.connect(self.insertCustomer)
                self.cancel = self.findChild(QPushButton, "cancelButton")
                self.cancel.clicked.connect(self.close)
                    
        import re

       
        def userExists(self, email, lastname, password):
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

           
            cursor.execute("select 1 from customers where (last_name = ? and email = ? and password = ? and account_type = ?);", (lastname, email ,password, "normal"))
           
            
            result = cursor.fetchone()
            connection.commit()
            connection.close()
            if result:
                return True
            else:
                return False


            
            
        def validate_email(self, email):
                    # Validate the email format
                    if "@" in email and ( email.endswith(".com") or "@st.habib.edu.pk" in email )and len(email) >= 10:
                        print(" Email is True hei")
                        return True
                    else:
                        return False
        def validate_name(self, name):
            check = name.isdigit()
            if len(name) >=3 and not(check):
                print("name is True hei")
                return True
            else:
                return False
        def validate_password(self,password):
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(not c.isalnum() for c in password)
            is_length_valid = len(password) >= 5

            if has_upper and has_lower and has_digit and has_special and is_length_valid:
               
                return True
            else:
                return False

            ## when the user enters their values insert a new user
        def insertCustomer(self):
                
                self.userEmail =  self.findChild(QLineEdit, "email").text()
                self.firstName =  self.findChild(QLineEdit, "firstname").text()
                self.lastName =   self.findChild(QLineEdit, "lastname").text()
                self.password_field = self.findChild(QLineEdit, "pass1").text()
            
                print(self.validate_email(self.userEmail))
                if (self.userEmail == ""
                    or self.firstName == "" 
                    or self.lastName == ""
                    or self.password_field == ""):
                        msg = QtWidgets.QMessageBox()
                        msg.setText("Please Enter All Required Attributes!")
                        msg.setWindowTitle("Error")
                        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                        msg.exec()
              
                elif  self.validate_email(self.userEmail) == False:
                        self.text = "Invalid Email!"
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle('Error')
                        self.error.setText(self.text)
                        self.error.show()
                elif  self.validate_name(self.lastName) == False:
                        self.text = "Please Enter a valid Name ! "
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle('Error')
                        self.error.setText(self.text)
                        self.error.show()
                elif  self.validate_password(self.password_field) == False:
                        self.text = " Password should contain Upper case, lower case, digit and special character ! "
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle('Error')
                        self.error.setText(self.text)
                        self.error.show()
                elif self.userExists(self.userEmail, self.lastName, self.password_field):
                        self.text = "User Already exists !"
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle('Error')
                        self.error.setText(self.text)
                        self.error.show()
                    
                else:
                    connection = pyodbc.connect(
                            connection_string
                        )

                    cursor = connection.cursor()
                    # print( self.userEmail,  self.password_field,  self.firstName,  self.lastName, "printed")
                    cursor.execute("INSERT INTO customers values(?,?,?,?);" , ( self.lastName,  self.userEmail,  self.password_field, 'normal'))
                    

                    # Retrieve the newly inserted customer ID
                    cursor.execute("select id, last_name from customers where id = (select max(id) from customers)")
                    result = cursor.fetchone()
                    customer_id = result[0]
                    customer_name = result[1]
                


                    # Show a message box with the customer ID
                    connection.commit()
                    connection.close()
                    QtWidgets.QMessageBox.information(
                        self, "customer Inserted", f"Customer ID : {customer_id} , Customer Name :{customer_name} has been inserted successfully.")
        # if the user enters some wrong values 
    
        def close(self):
            self.hide()
            
            
        # Close the database connection
       
        #   # login function  
      
                
        

    


