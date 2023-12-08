import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QComboBox, QLineEdit, QTableWidgetItem ,QRadioButton, QCheckBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import pyodbc
import Shopping

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


class UI(QtWidgets.QMainWindow):
    def __init__(self, customer_id):
    # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Catalogue_screen.ui', self)
        # Show the 
        self.customer_id = customer_id
        self.show()

        self.temp={}

        #Filtring the items 
        self.namebox=self.findChild(QComboBox, "Itemname")
        self.catbox=self.findChild(QComboBox, "Category_box") 
        self.searchi=self.findChild(QPushButton,"search_but")
        self.colorbox=self.findChild(QComboBox,"color_box")
        self.sizebox= self.findChild(QComboBox, "size_box")
        self.searchi.clicked.connect(self.Filter_screen)

        #pipolating catalogue
        self.populate_items_screen()

        #refreshing screen
        self.refresher=self.findChild(QPushButton,"refresh_but")
        self.refresher.clicked.connect(self.refresh_screen)

        #closing screen
        self.off=self.findChild(QPushButton,"close_but")
        self.off.clicked.connect(self.closing)
        
        #add to cart functionality
        self.carting=self.findChild(QPushButton, "cart_but")
        self.cart_but.setDisabled(True)
        self.tableWidget.itemClicked.connect(self.open_cart_screen)

    def open_cart_screen(self, item):
        row = item.row()
        self.columns_data = []
        self.cart_but.setDisabled(False)
       

        for col in range(self.tableWidget.columnCount()):
            self.columns_data.append(self.tableWidget.item(row, col).text()) 

        #here we have to connect carting button ro process the availiale information
       
        
        
        if self.columns_data is not None:
                
                self.carting.clicked.connect(self.openCart)
        else:     
            
            error_message = "Error: No row is selected."
            QMessageBox.critical(self, "Error", error_message)


        # QMessageBox.information(self, "Row Clicked", f"You clicked on row {row} with data: {columns_data}")

    def openCart(self):
                
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                for ele in self.columns_data:
                    print(ele , " <= data ")
                cart_info = (
                    int(self.columns_data[0]),
                    float(self.columns_data[-2]) - (float(self.columns_data[-1])),
                    float(self.columns_data[-1]),
                    float(self.columns_data[-2])
                    )
                
                                
                qu = "INSERT INTO cart (product_id, total, discount, gross_total) VALUES (?, ?, ?, ?)"
                cursor.execute(qu, cart_info)
                

                connection.commit()


                QMessageBox.information(self, "Success", "Product has been added to the cart successfully!")
                self.cart = Shopping.Shopping1(self.customer_id)
                self.cart.show()
               

                connection.close()
        
        
    def populate_items_screen(self):
            # inorder to populate the items you should have keys in product_brand bridge table AND items in brands and well categories.
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()       
        
        select_all_query = """
                SELECT
                p.id,
                p.name,
                c.name AS category_name,
                p.color,
                p.size,
                b.brand_name AS brand_name,
                p.[quantity_in_stock,],
                p.price,
                p.discount
                FROM products p
                JOIN product_brand pb ON p.id = pb.product_id
                JOIN brands b ON b.id = pb.brand_id
                JOIN categories c ON p.category = c.id;
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
                'ID':product_details[0],
                'name': product_details[1],
                'category': product_details[2],
                'color': product_details[3],
                'size': product_details[4],
                'brand': product_details[5],
                'price': product_details[7],
                'Discount':product_details[8]
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

    def refresh_screen(self):
        
        self.tableWidget.setRowCount(0)

        self.n = self.namebox.currentText()
        self.c = self.catbox.currentText()
        self.si = self.sizebox.currentText()
        self.co = self.colorbox.currentText()
        

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        select_all_query = """
                SELECT
                p.id,
                p.name,
                c.name AS category_name,
                p.color,
                p.size,
                b.brand_name AS brand_name,
                p.[quantity_in_stock,],
                p.price,
                p.discount
                FROM products p
                JOIN product_brand pb ON p.id = pb.product_id
                JOIN brands b ON b.id = pb.brand_id
                JOIN categories c ON p.category = c.id;
        """

        cursor.execute(select_all_query)

        # Fetch all rows
        all_products = cursor.fetchall()

        # Loop through the rows and print details
        for product_details in all_products:
            item_details = {
                'ID':product_details[0],
                'name': product_details[1],
                'category': product_details[2],
                'color': product_details[3],
                'size': product_details[4],
                'brand': product_details[5],
                'price': product_details[7],
                'Discount':product_details[8]
            }
            self.update_table(item_details)  
        
        connection.close()

    def update_table(self, item_details):
        # Add a new row to the table
        current_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row)

        # Fill in the table with the item details
        for column, (key, value) in enumerate(item_details.items()):
            item = QTableWidgetItem(str(value))
            self.tableWidget.setItem(current_row, column, item)

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
                p.name,
                c.name AS category_name,
                p.color,
                p.size,
                b.brand_name AS brand_name,
                p.[quantity_in_stock,],
                p.price
                FROM products p
                JOIN product_brand pb ON p.id = pb.product_id
                JOIN brands b ON b.id = pb.brand_id
                JOIN categories c ON p.category = c.id;
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

    def closing(self):
        self.close()

# # Create an instance of QtWidgets . QApplication
# app = QtWidgets.QApplication(sys.argv)
# window = UI() # Create an instance of our class
# app.exec() # Start the application



