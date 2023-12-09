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

