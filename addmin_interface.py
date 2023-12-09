import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QComboBox, QLineEdit, QTableWidgetItem ,QRadioButton, QCheckBox, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
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
        self.populateCols()
        # self.name = self.findChild(QLineEdit, "name")
        # self.color = self.findChild(QComboBox, "color")
        # self.size = self.findChild(QComboBox, "size")
        # self.brand = self.findChild(QLineEdit, "b")
        # self.discription = self.findChild(QLineEdit, "discription")
        # self.quantity = self.findChild(QLineEdit, "quantity")
        # self.category = self.findChild(QLineEdit, "category")
        # self.price = self.findChild(QLineEdit, "price")
        # self.discount = self.findChild(QLineEdit, "discount")
        self.clos=self.findChild(QPushButton,"close")
        self.save_button.clicked.connect(self.save_item)
        self.save_button.clicked.connect(self.insert_product)
        self.clos.clicked.connect(self.closing)

    def save_item(self):
     
        item_details = {
            'name': self.name.text(),
            'category': self.category.currentText()[0],
            'color': self.color.currentText(),
            'size': self.size.currentText(),
            'brand': self.brand.currentText()[0],
            'quantity': self.Quantity.value(),
            'price': self.price.text()

        }
        self.itemAdded.emit(item_details)
    def populateCols(self):
        
           
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        cursor.execute("SELECT id,name from categories;")
        # Fetch all the results and append each (id, name) tuple to the list
        
        self.sizeList=["S","M","L","XL","XS"]
        
        self.categoryList = []
        for row in cursor.fetchall():
            category_id = row[0]
            category_name = row[1]
            category_tuple = (category_id, category_name)
            self.categoryList.append(category_tuple)
        print("categories available",self.categoryList)
        
        self.colorList  =[
            'Red',
            'Blue',
            'Green',
            'Yellow',
            'Black',
            'White',
            'Orange',
            'Purple',
            'Pink',
            'Brown',
            'Gray',
            'Cyan',
            'Magenta',
            'Lime',
            'Teal',
            'Olive',
            'Maroon',
            'Navy',
            'Aquamarine',
            'Turquoise',
            'Silver',
            'Gold',
            'Indigo',
            'Violet',
            'Beige',
            'Tan',
            'Khaki',
            'Coral',
            'Salmon',
            'Slate',
            'Ivory',
            'Lavender',
            'Periwinkle',
            'Plum',
            'Mint',
            'Chartreuse',
            'Mauve',
            'Apricot',
            'Crimson',
            'Azure',
            'Sienna',
            'Cerulean'
        ]
        cursor.execute("select id, brand_name from brands;")
        self.brandsList =[]
        for row in cursor.fetchall():
            brand_id = row[0]
            brand_name = row[1]
            brand_tuple = (brand_id, brand_name)
            self.brandsList.append(brand_tuple)
        print("Brands available",self.brandsList)
        
                # Clear the existing items in the spin box
        self.category.clear()
        self.color.clear()
        self.brand.clear()
        # Add each category 
        for category in self.categoryList:
            self.category.addItem(str(category))  # Add category as an item
        # Add each brand 
        for brand in self.brandsList:
            self.brand.addItem(str(brand))  # Add brand as an item
        # Add each color 
        for color in self.colorList:
            self.color.addItem(str(color))  # Add color as an item
            #add each size
        for size in self.sizeList:
            self.size.addItem(str(size))  # Add size as an item
            
        
        self.name.setPlaceholderText("Enter Full name of product")
        self.category.setPlaceholderText("Enter the category ID")
        self.discription.setPlaceholderText("Enter product description ")
        # self.size.setPlaceholderText("e.g L for large, XL for extra small")
        # self.color.setPlaceholderText()
        self.price.setPlaceholderText("e.g 100.00")
        self.discount.setPlaceholderText("e.g 00.00")
            
        
        
    def insert_product(self):
       

        # sql_query = 'select categoryID from Category where categoryName = (?)'
        # cursor.execute(sql_query, (category,))
        # categoryID = cursor.fetchone()
        # categoryID = categoryID[0] if categoryID else None

      

        print("check point..")
   
        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        # self.name.setPlaceholderText("Enter Full name of product")
        # self.category.setPlaceholderText("Enter the category ID")
        # self.discription.setPlaceholderText("Enter product description ")
        # # self.size.setPlaceholderText("e.g L for large, XL for extra small")
        # # self.color.setPlaceholderText()
        # self.price.setPlaceholderText("e.g 100.00")
        # self.discount.setPlaceholderText("e.g 00.00")
        # self.quantity.setPlaceholderText("enter an integer value")
        # self.category.setPlaceholderText("Enter the category ID")
        # self.color.setPlaceholderText()
        
        self.msg = QtWidgets.QMessageBox()
        self.name_value =  self.name.text()  # Assuming Name is a varchar
        self.category_value =   (self.category.currentText() )[1]
        self.description_value =  self.discription.text()
        self.brand_value = (self.brand.currentText())[1]
        self.size_value = self.size.currentText()
        self.color_value = self.color.currentText()   
        self.price_value = self.price.text()
        self.discount_value = self.discount.text()
        self.quantity_value =  self.Quantity.value()
        
        print("second check point....")
        print(
        self.name_value ,
        self.category_value, 
        self.description_value ,
        self.brand_value ,
        self.size_value, 
        self.color_value ,
        self.price_value ,
        self.discount_value ,
        self.quantity_value )
        
        
        
        
        if self.name_value == '' or self.category_value == '' or self.description_value == '' or  self.size_value == '' or  self.price_value == '' or  self.quantity_value == '' or  self.discount_value == '':
            print("if")
            self.msg.setWindowTitle("Error")
            self.msg.setText("Please enter complete information.")   

        elif self.is_float(self.price_value) == False or self.is_float(self.discount_value) == False:
            print("1st elif if")
            self.msg.setWindowTitle("Error")
            self.msg.setText("Price and discounted value should be in decimal")   

        elif self.quantity_value == 0 :
            print("2nd elif if")
            self.msg.setWindowTitle("Error")
            self.msg.setText("Quantity can not be zero")
               


            
            
        else:
              print("else conditino")
              try:
                    new_product = (
                    # int(self.P_id.text()),  # Assuming ProductID is an integer
                        str(self.name_value),  # Assuming Name is a varchar
                        int(self.category_value) ,
                        str(self.description_value), 
                        str(self.size_value) ,
                        str(self.color_value) ,
                        float(self.price_value), 
                        float(self.discount_value), 
                        int(self.quantity_value )
                      
                    )
                    print("insert ki query se pehle",self.name_value)
                    
                    insert_query = """
                                    INSERT INTO products
                                    ( [name], [category], [description], [size], [color], [price], [discount], [quantity_in_stock,] )
                                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
                                """
                    
                    cursor.execute(insert_query, new_product)
                    print("insert ki query se baaad",self.name_value)
                    connection.commit()  # Commit the transaction
                    cursor.execute("SELECT TOP 1 id FROM products ORDER BY id DESC")
                    self.productid = cursor.fetchone()
                    print(self.productid,"<= newly inserted product id")
                    

                    # Extract the ID value from the tuple fetched
                    if self.productid:
                        
                        self.product_id1 = self.productid[0]  # Extracting the ID value
                        print(self.product_id1, 'productid1 to insert')
                        print(self.brand_value, "brand to insert")

                        # Insert into PRODUCT_BRANDS using the retrieved product_id and self.brand
                        insert_brand_query = "INSERT INTO PRODUCT_BRAND VALUES (?, ?)"
                        cursor.execute(insert_brand_query, (self.product_id1, self.brand_value))
                    
                
                        connection.commit()
                # Display a success message box
                        QMessageBox.information(self, "Success", "Product added successfully!")

                    # Clear all fields
             
                    self.name.clear()
                    self.category.setCurrentIndex(0)
                    self.discription.clear()
                    self.size.setCurrentIndex(0)  # Assuming the default index is 0
                    self.color.setCurrentIndex(0)  # Assuming the default index is 0
                    self.price.clear()
                    self.discount.clear()
                    self.Quantity.clear()
                    self.brand.setCurrentIndex(0)




              except Exception as e:
                    print(f"Error inserting product: {e}")

              finally:
                # Close the connection in the finally block to ensure it happens even if an exception occurs
                 connection.close()

    def is_float(self, value):
        if isinstance(value, str) and value.replace('.', '', 1).isdigit():
            return True
        return False
    def closing(self):
        self.hide() 

        
        


# # # Create an instance of QtWidgets . QApplication
# app = QtWidgets.QApplication(sys.argv)
# window = UI() # Create an instance of our class
# app.exec() # Start the application