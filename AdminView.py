import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import QDate
from AdminView_ui import Ui_MainWindow  # Import the generated class
import pyodbc  # pyodbc module

class AdminView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the signals of pushButton and pushButton_2 to functions
        self.pushButton.clicked.connect(self.clear_data)
        self.pushButton_2.clicked.connect(self.show_data)

    def clear_data(self):
        # Clear all table widgets
        self.tableWidget_2.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_5.setRowCount(0)

    def show_data(self):
        # Fetch and display data based on user input

        # Fetch and display data in "Items" group box
        selected_category = self.comboBox.currentText()
        self.populate_table(self.tableWidget_2, "Items", selected_category, ["ItemID", "Description"])

        # Fetch and display data in "Orders" group box
        selected_date = self.dateEdit.date().toString("yyyy-MM-dd")
        self.populate_table(self.tableWidget, "Orders", selected_date, ["OrderID", "CustomerID", "Total"])

        # Fetch and display data in "Customers" group box
        selected_customer_id = self.lineEdit.text()
        self.populate_table(self.tableWidget_3, "Customers", selected_customer_id, ["CustomerID", "Name", "Email"])

        # Fetch and display data in "Shippers" group box
        selected_shipper_id = self.lineEdit_2.text()
        self.populate_table(self.tableWidget_4, "Shippers", selected_shipper_id, ["ShipperID", "Name", "Contact"])

        # Fetch and display data in "Delivery Areas" group box
        selected_city = self.lineEdit_3.text()
        self.populate_table(self.tableWidget_5, "DeliveryAreas", selected_city, ["Area", "City"])

    def populate_table(self, table_widget, table_name, filter_value, columns):
        # Populate the table widget with data from the database

        # Replace these with your own database connection details
        server = 'your_server'
        database = 'your_database'
        username = 'your_username'
        password = 'your_password'

        # Create the connection string
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Connect to the database
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Build the SQL query based on whether a filter value is provided
        if filter_value:
            query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE {columns[0]} = ?"
            params = (filter_value,)
        else:
            query = f"SELECT {', '.join(columns)} FROM {table_name}"
            params = ()

        # Execute the query
        cursor.execute(query, params)

        # Fetch all rows and populate the table widget
        table_widget.setRowCount(0)
        for row_index, row_data in enumerate(cursor.fetchall()):
            table_widget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                table_widget.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

def main():
    app = QApplication(sys.argv)
    window = AdminView()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

