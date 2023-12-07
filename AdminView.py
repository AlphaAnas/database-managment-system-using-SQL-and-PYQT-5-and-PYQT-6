import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDateEdit, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QGroupBox, QMessageBox, QDialog, QVBoxLayout, QLabel
from PyQt5.uic import loadUi
import pyodbc

class AdminView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Establishing a connection to the database
        self.conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=MUSTAFA;'
            'DATABASE=POSHAAK;'
            'Trusted_Connection=yes;'
        )

        # Creating a cursor to execute SQL queries
        self.cursor = self.conn.cursor()

        # Loading the UI from the .ui file
        loadUi("AdminView.ui", self)

        # Connecting buttons to their respective functions
        self.ClearButton.clicked.connect(self.clear_data)
        self.ShowButton.clicked.connect(self.show_data)

        # Connecting delete buttons to their respective functions
        self.OrdersDeleteButton.clicked.connect(self.delete_selected_orders)
        self.ShippersDeleteButton.clicked.connect(self.delete_selected_shippers)
        self.CategoryDeleteButton.clicked.connect(self.delete_selected_categories)
        self.CustomersDeleteButton.clicked.connect(self.delete_selected_customers)
        self.DeliveryDeleteButton.clicked.connect(self.delete_selected_delivery_areas)

        # Connecting insert buttons to their respective functions
        self.ShipperInsertButton.clicked.connect(self.open_shipper_insert_window)
        self.CategoryInsertButton.clicked.connect(self.open_category_insert_window)
        self.DeliveryInsertButton.clicked.connect(self.open_delivery_insert_window)

        self.show_data()

    def clear_data(self):
        # Clearing data in all table widgets
        self.CategoriesTableWidget.setRowCount(0)
        self.OrdersTableWidget.setRowCount(0)
        self.CustomersTableWidget.setRowCount(0)
        self.ShippersTableWidget.setRowCount(0)
        self.DeliveryTableWidget.setRowCount(0)

    def show_data(self):
        # Clearing data before showing new data
        self.clear_data()

        # Retrieving data based on filters and populating table widgets
        self.show_categories()
        self.show_orders()
        self.show_customers()
        self.show_shippers()
        self.show_delivery_areas()

    def show_categories(self):
        # Getting the selected category from the CategoryComboBox
        selected_category = self.CategoryComboBox.currentText()

        # Constructing the SQL query based on the selected category
        if selected_category == "All":
            sql_query = "SELECT * FROM Categories"
        else:
            sql_query = f"SELECT * FROM Categories WHERE id = {selected_category}"

        # Executing the query and populating the CategoriesTableWidget
        self.cursor.execute(sql_query)
        for row_num, row_data in enumerate(self.cursor.fetchall()):
            self.CategoriesTableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.CategoriesTableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def show_orders(self):
        # Getting the selected date from the OrdersDateEdit
        selected_date = self.OrdersDateEdit.date().toString("yyyy-MM-dd")

        # Constructing the SQL query based on the selected date
        if selected_date == "2000-01-01":
            sql_query = "SELECT * FROM Orders"
        else:
            sql_query = f"SELECT * FROM Orders WHERE order_date = '{selected_date}'"

        # Executing the query and populating the OrdersTableWidget
        self.cursor.execute(sql_query)
        for row_num, row_data in enumerate(self.cursor.fetchall()):
            self.OrdersTableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.OrdersTableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def show_customers(self):
        # Getting the entered CustomerID from the CustomerIDLineEdit
        customer_id = self.CustomerIDLineEdit.text()

        # Constructing the SQL query based on the entered CustomerID
        if not customer_id:
            sql_query = "SELECT * FROM Customers"
        else:
            sql_query = f"SELECT * FROM Customers WHERE id = {customer_id}"

        # Executing the query and populating the CustomersTableWidget
        self.cursor.execute(sql_query)
        for row_num, row_data in enumerate(self.cursor.fetchall()):
            self.CustomersTableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.CustomersTableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def show_shippers(self):
        # Getting the entered ShipperID from the ShipperIDLineEdit
        shipper_id = self.ShipperIDLineEdit.text()

        # Constructing the SQL query based on the entered ShipperID
        if not shipper_id:
            sql_query = "SELECT * FROM Shippers"
        else:
            sql_query = f"SELECT * FROM Shippers WHERE id = {shipper_id}"

        # Executing the query and populating the ShippersTableWidget
        self.cursor.execute(sql_query)
        for row_num, row_data in enumerate(self.cursor.fetchall()):
            self.ShippersTableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.ShippersTableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def show_delivery_areas(self):
        # Getting the entered city from the CityLineEdit
        city = self.CityLineEdit.text()

        # Constructing the SQL query based on the entered city
        if not city:
            sql_query = "SELECT * FROM [Delivery Areas]"
        else:
            sql_query = f"SELECT * FROM [Delivery Areas] WHERE city = '{city}'"

        # Executing the query and populating the DeliveryTableWidget
        self.cursor.execute(sql_query)
        for row_num, row_data in enumerate(self.cursor.fetchall()):
            self.DeliveryTableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.DeliveryTableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def delete_selected_orders(self):
        # Get the selected row
        selected_row = self.OrdersTableWidget.currentRow()

        # Delete the selected row from the table widget
        if selected_row != -1:
            self.OrdersTableWidget.removeRow(selected_row)
            QMessageBox.information(self, "Delete Successful", "Order deleted successfully!")
        else:
            QMessageBox.warning(self, "Delete Warning", "Please select a row to delete.")

    def delete_selected_shippers(self):
        # Get the selected row
        selected_row = self.ShippersTableWidget.currentRow()

        # Delete the selected row from the table widget
        if selected_row != -1:
            self.ShippersTableWidget.removeRow(selected_row)
            QMessageBox.information(self, "Delete Successful", "Shipper deleted successfully!")
        else:
            QMessageBox.warning(self, "Delete Warning", "Please select a row to delete.")

    def delete_selected_categories(self):
        # Get the selected row
        selected_row = self.CategoriesTableWidget.currentRow()

        # Delete the selected row from the table widget
        if selected_row != -1:
            self.CategoriesTableWidget.removeRow(selected_row)
            QMessageBox.information(self, "Delete Successful", "Category deleted successfully!")
        else:
            QMessageBox.warning(self, "Delete Warning", "Please select a row to delete.")

    def delete_selected_customers(self):
        # Get the selected row
        selected_row = self.CustomersTableWidget.currentRow()

        # Delete the selected row from the table widget
        if selected_row != -1:
            self.CustomersTableWidget.removeRow(selected_row)
            QMessageBox.information(self, "Delete Successful", "Customer deleted successfully!")
        else:
            QMessageBox.warning(self, "Delete Warning", "Please select a row to delete.")

    def delete_selected_delivery_areas(self):
        # Get the selected row
        selected_row = self.DeliveryTableWidget.currentRow()

        # Delete the selected row from the table widget
        if selected_row != -1:
            self.DeliveryTableWidget.removeRow(selected_row)
            QMessageBox.information(self, "Delete Successful", "Delivery Area deleted successfully!")
        else:
            QMessageBox.warning(self, "Delete Warning", "Please select a row to delete.")

    def open_shipper_insert_window(self):
        # Open the ShipperInsert window
        self.shipper_insert_window = ShipperInsertWindow(self)
        self.shipper_insert_window.show()

    def open_category_insert_window(self):
        # Open the CategoryInsert window
        self.category_insert_window = CategoryInsertWindow(self)
        self.category_insert_window.show()

    def open_delivery_insert_window(self):
        # Open the DeliveryInsert window
        self.delivery_insert_window = DeliveryInsertWindow(self)
        self.delivery_insert_window.show()

    def closeEvent(self, event):
        # Closing the database connection when the application is closed
        self.conn.close()
        event.accept()

class ShipperInsertWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ShipperInsertWindow, self).__init__(parent)
        loadUi("ShipperInsert.ui", self)

        # Connect button to function
        self.InsertButton.clicked.connect(self.insert_shipper)

        # Save the reference to the parent
        self.parent = parent

    def insert_shipper(self):
        # Get data from line edits
        shipper_id = self.IDLineEdit.text()
        shipper_name = self.NameLineEdit.text()
        contact_number = self.ContactLineEdit.text()
        email = self.EmailLineEdit.text()

        # Validate data types and insert into the Shippers table
        try:
            shipper_id = int(shipper_id)
            contact_number = int(contact_number)
            # Ensure other validations as needed for your specific case

            # Insert data into the Shippers table
            sql_query = f"INSERT INTO Shippers (id, name, contact_number, email) VALUES ({shipper_id}, '{shipper_name}', {contact_number}, '{email}')"
            self.parent.cursor.execute(sql_query)
            self.parent.conn.commit()

            QMessageBox.information(self, "Insert Successful", "Shipper inserted successfully!")
            self.close()

        except ValueError:
            QMessageBox.warning(self, "Insert Warning", "Invalid data types. Please enter valid data.")


class CategoryInsertWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CategoryInsertWindow, self).__init__(parent)
        loadUi("CategoryInsert.ui", self)

        # Connect button to function
        self.InsertButton.clicked.connect(self.insert_category)
        self.parent = parent  # Save the reference to the parent

    def insert_category(self):
        # Get data from line edits
        category_id = self.IDLineEdit.text()
        category_name = self.NameLineEdit.text()
        category_description = self.DesLineEdit.text()

        # Validate data types and insert into the Categories table
        try:
            category_id = int(category_id)
            # Ensure other validations as needed for your specific case

            # Insert data into the Categories table
            sql_query = f"INSERT INTO Categories (id, name, description) VALUES ({category_id}, '{category_name}', '{category_description}')"
            self.parent.cursor.execute(sql_query)
            self.parent.conn.commit()

            QMessageBox.information(self, "Insert Successful", "Category inserted successfully!")
            self.close()

        except ValueError:
            QMessageBox.warning(self, "Insert Warning", "Invalid data types. Please enter valid data.")


class DeliveryInsertWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DeliveryInsertWindow, self).__init__(parent)
        loadUi("DeliveryInsert.ui", self)

        # Connect button to function
        self.InsertButton.clicked.connect(self.insert_delivery_area)
        self.parent = parent  # Save the reference to the parent

    def insert_delivery_area(self):
        # Get data from line edits
        city = self.CityLineEdit.text()
        area = self.AreaLineEdit.text()
        country = self.CountryLineEdit.text()
        postal_code = self.PostalLineEdit.text()
        delivery_charges = self.ChargesLineEdit.text()
        possible = self.PossibleLineEdit.text()

        # Validate data types and insert into the [Delivery Areas] table
        try:
            delivery_charges = float(delivery_charges)  # Assuming charges are in float format
            # Ensure other validations as needed for your specific case

            # Insert data into the [Delivery Areas] table
            sql_query = f"INSERT INTO [Delivery Areas] (city, area, country, postal_code, delivery_charges, possible) " \
                        f"VALUES ('{city}', '{area}', '{country}', '{postal_code}', {delivery_charges}, {possible})"
            self.parent.cursor.execute(sql_query)
            self.parent.conn.commit()

            QMessageBox.information(self, "Insert Successful", "Delivery Area inserted successfully!")
            self.close()

        except ValueError:
            QMessageBox.warning(self, "Insert Warning", "Invalid data types. Please enter valid data.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminView()
    window.show()
    sys.exit(app.exec())

