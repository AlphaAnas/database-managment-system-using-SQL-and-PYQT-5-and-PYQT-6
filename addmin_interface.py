import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QComboBox, QLineEdit, QTableWidgetItem ,QRadioButton, QCheckBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import pyodbc


# Replace these with your own database connection details
server = 'DESKTOP-QJN0C6R\SHAPATER'
database = 'POSHAAK'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication
username = ''  # Specify a username if not using Windows Authentication
password = ''  # Specify a password if not using Windows Authentication


# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'





class UI(QtWidgets.QMainWindow):
    def __init__(self):
    # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Admin_interface.ui', self)
        # Show the GUI
        self.show()

        # Connect the view function with the view button.
        self.add_but=self.findChild(QPushButton, "Add_item")
        self.add_but.clicked.connect(self.additem)

        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")

        self.temp={}

        #Filtring the items 
        self.namebox=self.findChild(QComboBox, "Itemname")
        self.catbox=self.findChild(QComboBox, "cato") 
        self.searchi=self.findChild(QPushButton,"search_but")
        self.colorbox=self.findChild(QComboBox,"color")
        self.sizebox= self.findChild(QComboBox, "size")
        self.searchi.clicked.connect(self.Filter_screen)
             
        #for populating the screen with products of all kinds
        self.populate_items_screen()

        #delete product functinality
        self.dell=self.findChild(QPushButton,"delete_but")
        self.dell.clicked.connect(self.delete_item)

        #finally close the screen
        self.closing=self.findChild(QPushButton,"close_but")
        self.closing.clicked.connect(self.closeee)



 



    def populate_items_screen(self):
            # inorder to populate the items you should have keys in product_brand bridge table AND items in brands and well categories.
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()       
        
        select_all_query = """
            SELECT 
                [name], 
                [category], 
                [color], 
                [size], 
                [brand_id], 
                [quantity_in_stock,], 
                [price]
            FROM products
            JOIN product_brand ON products.id = product_brand.product_id
        """


        cursor.execute(select_all_query)

        # Fetch all rows
        all_products = cursor.fetchall()

        #intiing the color and size box with
        self.colorbox.addItem("None")
        self.sizebox.addItem("None")

        # Loop through the rows and print details
        for product_details in all_products:
            item_details = {
                'name': product_details[0],
                'category': product_details[1],
                'color': product_details[2],
                'size': product_details[3],
                'brand': product_details[4],
                'quantity': product_details[5],
                'price': product_details[6]
            }
            self.update_table(item_details)

            self.colorbox.addItem(str(item_details['color']))
            self.sizebox.addItem(str(item_details['size']))
            #this will populate combo_boxes of size and category
            if item_details['category'] not in self.temp:
                self.temp[item_details['category']]=["None",item_details['name']]
            else:
                self.temp[item_details['category']].append(item_details['name'])


        for i in self.temp:
            self.catbox.addItem(str(i), self.temp[i])

        self.catbox.activated.connect(self.clicker)
        connection.close()

    def clicker(self, index):
        self.namebox.clear()
        self.namebox.addItems(self.catbox.itemData(index))


    def Filter_screen(self):
        self.tableWidget.setRowCount(0)

        self.n = self.namebox.currentText()
        self.c = self.catbox.currentText()
        self.si = self.sizebox.currentText()
        self.co = self.colorbox.currentText()
        

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        select_all_query = """
            SELECT 
                [name], 
                [category], 
                [color], 
                [size], 
                [brand_id], 
                [quantity_in_stock,], 
                [price]
            FROM products
            JOIN product_brand ON products.id = product_brand.product_id
        """

        cursor.execute(select_all_query)

        # Fetch all rows
        all_products = cursor.fetchall()

        # Loop through the rows and print details
        for product_details in all_products:
            item_details = {
                'name': product_details[0],
                'category': product_details[1],
                'color': product_details[2],
                'size': product_details[3],
                'brand': product_details[4],
                'quantity': product_details[5],
                'price': product_details[6]
            }

            
            if (self.c == str(item_details["category"]) and self.n == "None" and self.si == "None" and self.co == "None"):
                self.update_table(item_details)
               

            elif (self.c == str(item_details["category"]) and self.n == item_details["name"] and self.si == "None" and self.co == "None"):
                self.update_table(item_details)
                

            elif (self.c == str(item_details["category"]) and self.n == item_details["name"] and self.si == item_details["size"] and self.co == "None"):
                self.update_table(item_details)
                
            elif (self.c == str(item_details["category"]) and self.n == item_details["name"] and self.si == item_details["size"] and self.co == item_details["color"]):
                self.update_table(item_details)
                

        connection.close()



    def additem(self):
        self.sec_form = addScreen()
        self.sec_form.itemAdded.connect(self.update_table)
        self.sec_form.show()
    
    def update_table(self, item_details):
        # Add a new row to the table
        current_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row)

        # Fill in the table with the item details
        for column, (key, value) in enumerate(item_details.items()):
            item = QTableWidgetItem(str(value))
            self.tableWidget.setItem(current_row, column, item)
        
    def delete_item(self):

        self.n=self.namebox.currentText()
        self.c=self.catbox.currentText()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()


        qeury1 = """
                DELETE FROM product_brand
                WHERE product_id IN (SELECT id FROM products WHERE category = ? AND name = ?) 
                """
        query2="""
                DELETE FROM products WHERE category = ? AND name = ?
            """
        #deletig from produc_brand table
        cursor.execute(qeury1, int(self.catbox.currentText()), self.namebox.currentText())
        #deleting from products Table
        cursor.execute(query2, int(self.catbox.currentText()), self.namebox.currentText())
        # Commit the changes
        connection.commit()
        # Display a success message box
        QMessageBox.information(self, "Success", "Product deleted successfully!")

        connection.close()

    def closeee(self):
        self.close()
        

class addScreen(QtWidgets.QMainWindow):
    itemAdded = pyqtSignal(dict) 
    def __init__(self):
    # Call the inherited classes __init__ method
        super().__init__()
        # Load the .ui file
        uic.loadUi('Admin_interface2.ui', self)

        self.setWindowTitle("Add Item")


        
        self.save_button = self.findChild(QPushButton, "add_but")
        self.P_id = self.findChild(QLineEdit, "product_id")
        self.name = self.findChild(QLineEdit, "name")
        self.color = self.findChild(QComboBox, "color")
        self.sizee = self.findChild(QComboBox, "size")
        self.brand = self.findChild(QLineEdit, "b")
        self.discription = self.findChild(QLineEdit, "discription")
        self.quantity = self.findChild(QLineEdit, "quantity")
        self.category = self.findChild(QLineEdit, "category")
        self.price = self.findChild(QLineEdit, "price")
        self.discount = self.findChild(QLineEdit, "discount")
        self.clos=self.findChild(QPushButton,"close")
        self.save_button.clicked.connect(self.save_item)
        self.save_button.clicked.connect(self.insert_product)
        self.clos.clicked.connect(self.closing)

    def save_item(self):
        item_details = {
            'name': self.name.text(),
            'category': self.category.text(),
            'color': self.color.currentText(),
            'size': self.sizee.currentText(),
            'brand': self.brand.text(),
            'quantity': self.quantity.text(),
            'price': self.price.text()

        }
        self.itemAdded.emit(item_details)

    def insert_product(self):
        print("check point..")
        try:
            # Establish a connection to the database
            connection = pyodbc.connect(connection_string)

            # Create a cursor to interact with the database
            cursor = connection.cursor()

            new_product = (
                int(self.P_id.text()),  # Assuming ProductID is an integer
                str(self.name.text()),  # Assuming Name is a varchar
                str(self.category.text()),  # Assuming Category is a varchar
                str(self.discription.text()),  # Assuming Description is text
                str(self.sizee.currentText()),  # Assuming Size is char
                str(self.color.currentText()),  # Assuming Color is varchar
                float(self.price.text()),  # Assuming Price is a float
                float(self.discount.text()),  # Assuming Discount is a double
                int(self.quantity.text())  # Assuming Quantity is an integer
            )
            
            insert_query = """
                            INSERT INTO products
                            ([id], [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,] )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """
            cursor.execute(insert_query, new_product)
            connection.commit()  # Commit the transaction

            # Display a success message box
            QMessageBox.information(self, "Success", "Product added successfully!")

            # Clear all fields
            self.P_id.clear()
            self.name.clear()
            self.category.clear()
            self.discription.clear()
            self.sizee.setCurrentIndex(0)  # Assuming the default index is 0
            self.color.setCurrentIndex(0)  # Assuming the default index is 0
            self.price.clear()
            self.discount.clear()
            self.quantity.clear()
            self.brand.clear()




        except Exception as e:
            print(f"Error inserting product: {e}")

        finally:
            # Close the connection in the finally block to ensure it happens even if an exception occurs
            connection.close()


    def closing(self):
        self.hide() 

        
        


# Create an instance of QtWidgets . QApplication
app = QtWidgets.QApplication(sys.argv)
window = UI() # Create an instance of our class
app.exec() # Start the application