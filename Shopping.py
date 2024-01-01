# Importing essential modules
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import Payment
import lastscreen
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

class Shopping1(QtWidgets.QMainWindow):
    def __init__(self, customer_id):
         # Call the inherited classes __init__ method
        super(Shopping1, self).__init__() 
        # Load the .ui file
        uic.loadUi('Shopping.ui', self) 
        self.setWindowTitle("Shopping Cart")
        self.rows = 0
        self.total_bill_amount =0 
    
        self.customer_id = customer_id
        print(self.customer_id , "yeh dekho ")
      
        self.populate_items_screen()
        
        self.total_bill_amount = self.calculate_bill()  # this function will itself calculate  the total amount now with discount
        self.total.setText(str(self.total_bill_amount)) 

        
        
             
        # funcionality of delete and back buttons
        
        self.backButton.clicked.connect(self.back)
        self.deleteButton.clicked.connect(self.delete)
     
        
        
        # checkout and continue button functionality
        
        self.continueButton.clicked.connect(self.back)
       
        self.checkoutButton1 = self.findChild(QPushButton, "checkoutButton")
        self.checkoutButton1.clicked.connect(self.paymentWindow)
            

                # TODO: Write SQL query to fetch orders data
                
 # ... (previous code)
    def populate_items_screen(self):
        connection = pyodbc.connect(connection_string)
      

        cursor = connection.cursor()
        cursor.execute("select count(entry_id) as number from cart; " )
        number = cursor.fetchone()
        self.rows = number[0] # Store the total number of rows to display

        
          
        print(self.customer_id, 'customer id2')
        cursor.execute( " SELECT ALL product_id FROM cart WHERE customer_id = ?;", self.customer_id)
       
        entry_ids = cursor.fetchall()
      
      
    
        for entry_id in entry_ids:
            entry_id = entry_id[0]
            print(entry_id, "entry ids in cart")
            cursor.execute("SELECT * FROM products WHERE id = ?", entry_id)
            product_details = cursor.fetchone()
            if product_details:  
                self.products_data = {
                    'ID': product_details[0],
                    'name': product_details[1],
                    'category': product_details[2],
                    'description': product_details[3],   
                    'size' : product_details[4],             
                    'color': product_details[5],
                    'price': product_details[6],
                    'discount': product_details[7]
                    
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
        print("update table called")
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
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("select count(entry_id) as number from cart where customer_id = ?; ",self.customer_id )
        number = cursor.fetchone()
        print("elements in the cart : ", number)
        if number[0] == 0:
            warning = QMessageBox(self)
            warning.setWindowTitle("Warning")
            warning.setText(f"Can not delete from empty cart!! ")
            warning.setStandardButtons(QMessageBox.StandardButton.Ok)
            warning.setIcon(QMessageBox.Icon.Warning)
            dlg = warning.exec()
            return
        connection.close()
        selected_indexes =None            
        selected_indexes = self.itemWidget.selectedIndexes()
        print(selected_indexes)
        if selected_indexes == None or selected_indexes == []:
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Invalid !")
                    warning.setText("Please select a row to delete !! ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    warning.setIcon(QMessageBox.Icon.Warning)
                    dlg = warning.exec()
        else:
            
                if len(selected_indexes) >= 0:
                    for primary_key_item in selected_indexes:
                        row = primary_key_item.row() 
                        print(primary_key_item , "item to be deleted")
                        primary_key_item = self.itemWidget.item(row, 0)  # Assuming primary key is in the first column (index 0)
                        if primary_key_item is not None:
                            primary_key_value = primary_key_item.text()
                            print(primary_key_value)
                            if self.show_warning:
                            
                                # Delete from the database
                                connection = pyodbc.connect(connection_string)
                                cursor = connection.cursor()
                                cursor.execute("DELETE FROM cart WHERE product_id = ?", primary_key_value)
                                connection.commit()
                                connection.close()

                                print("deleted id is : ", primary_key_value)
                                # Hide row in the UI instead of removing it
                                self.itemWidget.hideRow(row)
                            
                                
                                # Remove row from the UI
                                # self.itemWidget.removeRow(selected_row)
                                msg = QtWidgets.QMessageBox()
                                msg.setText(f"product deleted with id = {primary_key_value}")
                                msg.setWindowTitle("Item Deleted")
                                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                                msg.exec()
                                
                                # Recalculate the total bill after deletion
                                total_bill_amount = self.calculate_bill()

                                self.total.setText(str(total_bill_amount))
                            
                       
                          
            
           

                
              
            # proceed to payment window
    def paymentWindow(self):
      
                  
                    try:
                        connection = pyodbc.connect(connection_string)
                        cursor = connection.cursor()

                        cursor.execute("SELECT * FROM cart WHERE customer_id = ?;", self.customer_id)
                        elements = cursor.fetchall()

                        if elements:
                            for ele in elements:  # Iterate through fetched elements, not self.elements
                                self.grossTotal = ele[-1]
                                self.paymentMethod = "cash"
                                self.status = "pending"
                                self.shipDate ='still None'
                                self.shipVia = "PAKISTAN POST" # default is Pak post else the admin can edit it
                                self.shipperID = 1
                                # Get the current date
                                current_date = QDate.currentDate()

                                # Get the complete date as a formatted string (YYYY-MM-DD)
                                self.formatted_date = current_date.toString("yyyy-MM-dd")

                               
                                cursor.execute("INSERT INTO ORDERS values(?,?,?,?,?,?,?,?)",self.customer_id, self.formatted_date, self.grossTotal,self.paymentMethod, self.status, self.shipDate, self.shipVia,self.shipperID )
                                cursor.commit()
                                cursor.execute("select max(order_id) from orders where customer_id = ?", self.customer_id)
                                self.orderid = cursor.fetchone()[0]
                                if self.orderid>0:
                                    self.flag = True
                            if self.flag:
                                warning = QMessageBox(self)
                                warning.setWindowTitle("Order Placed")
                                warning.setText(f"Your order has been placed with orderID {self.orderid} !! ")
                                warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                                warning.setIcon(QMessageBox.Icon.Warning)
                                dlg = warning.exec()
                            else:
                                warning = QMessageBox(self)
                                warning.setWindowTitle("Order Aborted! ")
                                warning.setText(f"Your order has been aborted ! we are very sorry for inconvenience! Check again other time ")
                                warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                                warning.setIcon(QMessageBox.Icon.Warning)
                                dlg = warning.exec()
                            
                            
                            cursor.execute("DELETE FROM CART")
                            print("all Elements deleted from cart for the customer :",self.customer_id)
                            self.LASTSCREEN = lastscreen.lastclass(self.orderid)
                            self.LASTSCREEN.show()
                        else:
                                warning = QMessageBox(self)
                                warning.setWindowTitle("Empty Cart")
                                warning.setText("Please insert a product in your cart first !! ")
                                warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                                warning.setIcon(QMessageBox.Icon.Warning)
                                dlg = warning.exec()
                                        
                                
            

                 
                    except pyodbc.Error as e:
                        print("Error:", e)  # Handle the exception appropriately

                    finally:
                        if 'connection' in locals():
                            connection.close()  # Close the connection in the finally block

                    
          
    def show_warning(self, flag):
                    
                    warning = QMessageBox(self)
                    warning.setWindowTitle("Message Box")
                    warning.setText("Are you sure you want to delete this row !! ")
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
                    warning.setIcon(QMessageBox.Icon.Warning)
                    dlg = warning.exec()
                    if dlg == QMessageBox.StandardButton.Ok:
                        flag=True
                        return flag
                    
    def calculate_bill(self):
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                
                cursor.execute("SELECT SUM(ROUND(gross_total, 2)) FROM cart where customer_id = ?",self.customer_id)
                
                # Fetch the result and store it in a variable
                total_bill_result = cursor.fetchone()
                self.total_bill_amount = total_bill_result[0] if total_bill_result[0] is not None else 0
                self.total_bill_amount = round(self.total_bill_amount, 2)  # Round to two decimal places
                
            except pyodbc.Error as e:
                print("Error:", e)
                self.total_bill_amount = 0
            
            finally:
                if 'connection' in locals():
                    connection.close()
            
            return self.total_bill_amount

     
        
    
    
        
    
        

        
        
def main(): 
    app = QApplication(sys.argv)
    window = Shopping1(2)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
