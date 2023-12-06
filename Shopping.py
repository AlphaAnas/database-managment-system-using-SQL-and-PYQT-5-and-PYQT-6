# Importing essential modules
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import Payment
import pyodbc

# # Replace these with your own database connection details
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

class Shopping(QtWidgets.QMainWindow):
    def __init__(self):
         # Call the inherited classes __init__ method
        super(Shopping, self).__init__() 
        # Load the .ui file
        uic.loadUi('Shopping.ui', self) 
        
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()

                # TODO: Write SQL query to fetch orders data
        
        cursor.execute("select count(id) as number from products; " )
        number = cursor.fetchone()
        rows = number[0] #store the total number of rows to display
        
        cursor.execute("select* from products;")
        products_data = cursor.fetchall()
        print(products_data) # a list of tuples containing all the 
        
       
       
        # populating the cart
        self.itemWidget.setRowCount(rows)
        for i, row_data in enumerate(products_data):
                for j, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))  # Convert data to string and create a QTableWidgetItem
                        if j != 8:
                            self.itemWidget.setItem(i, j, item)  # Set the item in the QTableWidget

                        # Make the items non-editable
                            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
       
            
                # Spread columns to fill the entire widget

        header = self.itemWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive) 
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch) #description wale ko column ko stretch kro
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6,QHeaderView.ResizeMode.ResizeToContents)
        
        
        # cursor.execute("SELECT SUM(total - discount) AS total_bill_amount FROM cart c")
        
        
        # # Fetch the result and store it in a variable
        # total_bill_result = cursor.fetchone()
        # total_bill_amount = total_bill_result[0]
        # total_bill_amount = self.calculate_bill()
        # self.total.setText(str(total_bill_amount))
    
        
        total_bill_amount = self.calculate_bill()  # this function will itself calculate  the total amount now with discount
        self.total.setText(str(total_bill_amount)) 

        
        
             
        # funcionality of delete and back buttons
        
        self.backButton.clicked.connect(self.back)
        self.deleteButton.clicked.connect(self.delete)
        
        
        # checkout and continue button functionality
        
        self.continueButton.clicked.connect(self.customerWindow)
        self.checkoutButton.clicked.connect(self.paymentWindow)
            
        connection.commit()
        
   
        
    def back(self):
        self.hide()
        
    def delete(self):
        selected_row = self.itemWidget.currentRow()
        if selected_row == None:
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Invalid !")
                    warning.setText("Please select a row to delete !! ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    warning.setIcon(QMessageBox.Icon.Warning)
                    dlg = warning.exec()
        else:
            
                if selected_row >= 0:
                    primary_key_item = self.itemWidget.item(selected_row, 0)  # Assuming primary key is in the first column (index 0)
                    if primary_key_item is not None:
                        primary_key_value = primary_key_item.text()
                        
                        # Delete from the database
                        connection = pyodbc.connect(connection_string)
                        cursor = connection.cursor()
                        cursor.execute("DELETE FROM cart WHERE entry_id = ?", primary_key_value)
                        connection.commit()
                        
                        # Remove row from the UI
                        self.itemWidget.removeRow(selected_row)
                        
                        # Recalculate the total bill after deletion
                        total_bill_amount = self.calculate_bill()
                        self.total.setText(str(total_bill_amount))
                        
                        connection.commit()

            
           

                
              
            # proceed to payment window
    def paymentWindow(self):
        
        self.signup1 = Payment.MakePayment()
        self.signup1.show()
        
    def customerWindow(self):
          uic.loadUi("newScreen.ui",self)
          
    def show_warning(self, flag):
                    
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Message Box")
                    warning.setText("Are you sure you want to delete this row !! ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    warning.setIcon(QMessageBox.Icon.Warning)
                    dlg = warning.exec()
                    if dlg == QMessageBox.StandardButton.Ok:
                        flag=True
                        return flag
                    
    def calculate_bill(self):
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
             
        cursor.execute("SELECT SUM(total - discount) AS total_bill_amount FROM cart c")
        
        
        # Fetch the result and store it in a variable
        total_bill_result = cursor.fetchone()
        total_bill_amount = total_bill_result[0]
        
        connection.commit()
        return str(total_bill_amount)
     
        
    
    
        
    
        

        
        
def main(): 
    app = QApplication(sys.argv)
    window = Shopping()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
