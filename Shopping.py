# Importing essential modules
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import Payment
import pyodbc

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

class Shopping1(QtWidgets.QMainWindow):
    def __init__(self, customer_id):
         # Call the inherited classes __init__ method
        super(Shopping1, self).__init__() 
        # Load the .ui file
        uic.loadUi('Shopping.ui', self) 
    
        
    
        self.customer_id = customer_id
        print(self.customer_id , "yeh dekho ")
      
        self.populate_items_screen()
        
        total_bill_amount = self.calculate_bill()  # this function will itself calculate  the total amount now with discount
        self.total.setText(str(total_bill_amount)) 

        
        
             
        # funcionality of delete and back buttons
        
        self.backButton.clicked.connect(self.back)
        self.deleteButton.clicked.connect(self.delete)
        
        
        # checkout and continue button functionality
        
        self.continueButton.clicked.connect(self.back)
       
        self.checkoutButton1 = self.findChild(QPushButton, "checkoutButton")
        self.checkoutButton1.clicked.connect(self.paymentWindow())
            

                # TODO: Write SQL query to fetch orders data
                
 # ... (previous code)
    def populate_items_screen(self):
        connection = pyodbc.connect(connection_string)
      

        cursor = connection.cursor()
        cursor.execute("select count(entry_id) as number from cart; " )
        number = cursor.fetchone()
        self.rows = number[0] # Store the total number of rows to display

        
          
        print(self.customer_id, 'customer id2')
        cursor.execute( " SELECT product_id FROM cart WHERE customer_id = ?  GROUP BY product_id;", self.customer_id)
       
        entry_ids = cursor.fetchall()
      
      
        print(entry_ids,'nhi bhai')
    
        for entry_id in entry_ids:
            entry_id = entry_id[0]
            print(entry_id)
            cursor.execute("SELECT * FROM products WHERE id = ?", entry_id)
            product_details = cursor.fetchone()
            if product_details:  
                self.products_data = {
                    'ID': product_details[0],
                    'name': product_details[1],
                    'Description': product_details[2],
                    'size': product_details[3],                
                    'color': product_details[4],
                    'price': product_details[5],
                    'discount': product_details[7],
                }

                self.update_table(self.products_data)  # Update your table or interface here

        connection.commit()
        connection.close()

        # populating the cart



        
        
        # cursor.execute("SELECT SUM(total - discount) AS total_bill_amount FROM cart c")
        
        
        # # Fetch the result and store it in a variable
        # total_bill_result = cursor.fetchone()
        # total_bill_amount = total_bill_result[0]
        # total_bill_amount = self.calculate_bill()
        # self.total.setText(str(total_bill_amount))
    
        
        
       
        
   
    def update_table(self, item_details):
        # Add a new row to the table
        current_row = self.itemWidget.rowCount()
        self.itemWidget.insertRow(current_row)   
                # Fill in the table with the item details
     
        # Fill in the table with the item details
        print("xhala")
        for column, (key, value) in enumerate(item_details.items()):
            item = QTableWidgetItem(str(value))
            self.itemWidget.setItem(current_row, column, item)

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
                        print(primary_key_value)
                        
                        # Delete from the database
                        connection = pyodbc.connect(connection_string)
                        cursor = connection.cursor()
                        cursor.execute("DELETE FROM cart WHERE product_id = ?", primary_key_value)
                        print("id is : ", primary_key_value)
                        connection.commit()
                        
                        # Remove row from the UI
                        self.itemWidget.removeRow(selected_row)
                        msg = QtWidgets.QMessageBox()
                        msg.setText(f"product deleted with id = {primary_key_value}")
                        msg.setWindowTitle("Item Deleted")
                        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                        msg.exec()
                        
                        # Recalculate the total bill after deletion
                        total_bill_amount = self.calculate_bill()

                        self.total.setText(str(total_bill_amount))
                        
                        connection.commit()
                        connection.close()

            
           

                
              
            # proceed to payment window
    def paymentWindow(self):
      
                    connection = pyodbc.connect(connection_string)

                    cursor = connection.cursor()
                    
                    # cursor.execute("INSERT INTO orders (entry_id , customer_id) values (14, ?)", self.customer_id)
                    
                    
                    
                    cursor.commit()
                    
                    connection.close()
                    
                 
        
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Order Placed")
                    warning.setText("Your order has been placed with orderID !! ", 46)
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    warning.setIcon(QMessageBox.Icon.Warning)
                    dlg = warning.exec()
        
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
        print(total_bill_result, "yahan bill")
        total_bill_amount = total_bill_result[0]
        
        connection.commit()
        connection.close()
        return (total_bill_amount)
     
        
    
    
        
    
        

        
        
def main(): 
    app = QApplication(sys.argv)
    window = Shopping1(2)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
