# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import pyodbc

class CustomerInterface(QtWidgets.QMainWindow):
        def __init__(self):
            # Call the inherited classes __init__ method
            super(CustomerInterface, self).__init__() 
           




        # Load the .ui file
        def signup(self):
                uic.loadUi("signup_Form.ui",self)
            
                self.userEmail =  self.findChild(QLineEdit, "email").text()
                self.firstName =  self.findChild(QLineEdit, "firstname").text()
                self.lastName =   self.findChild(QLineEdit, "lastname").text()
                self.password_field = self.findChild(QLineEdit, "pass")
                self.password = self.password_field.text()
                self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
                print(self.firstName)

                self.signupButton1 = self.findChild(QPushButton, "signupButton")
                print(self.signupButton1)  # Check if this prints the correct button
                self.signupButton1.clicked.connect(self.insertCustomer)
                self.cancel = self.findChild(QPushButton, "cancelButton")
                self.cancel.clicked.connect(self.close)

            

                

            ## when the user enters their values insert a new user
        def insertCustomer(self):
                connection = pyodbc.connect(
                        connection_string
                    )

                cursor = connection.cursor()
                print( self.userEmail,  self.password,  self.firstName,  self.lastName)
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
    
        def close():
            print("close function xhalana hei ")
            
        # Close the database connection
       
        #   # login function  
        def login(self):
            userName=  self.findChild(QLineEdit,"userName").text()# if nothing is entered then value is ''
            user_password = self.findChild(QLineEdit,"password").text()  ##  if nothing is entered then value is ''
        



            connection = pyodbc.connect(
                    connection_string
                )

            cursor = connection.cursor()

                # TODO: Write SQL query to fetch orders data
        
            cursor.execute("SELECT CASE WHEN EXISTS (SELECT 1 FROM customers WHERE last_name = ? AND password = ?) THEN CAST(1 AS BIT) ELSE CAST(0 AS BIT) END AS UserExists;", (userName, user_password))

            
            user_exists = cursor.fetchone()[0]  # Fetch the result of EXISTS check
            connection.close()
            if(user_exists == True):
                    print("helookljdlfk;a")
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Message Box")
                    warning.setText("Login successful ! ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    warning.setIcon(QMessageBox.Icon.Information)
                    dlg = warning.exec()
                    self.customerInterface = CustomerInterface()
                    self.customerInterface.show()

            else:
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Message Box")
                    warning.setText("incorrect email or password ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok and QMessageBox.StandardButton.Close)
                    warning.setIcon(QMessageBox.Icon.Information)
                    dlg = warning.exec()
        

                    
                
        

    


