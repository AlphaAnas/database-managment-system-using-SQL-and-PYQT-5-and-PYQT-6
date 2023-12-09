
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate,QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QLineEdit,QMessageBox
import sys
import connection_string
import Payment
import pyodbc




class lastclass(QtWidgets.QMainWindow):
    def __init__(self, tracking):
        # Call the inherited classes __init__ method
        super(lastclass, self).__init__() 
    
        uic.loadUi('newScreen.ui', self) 
        self.text.setReadOnly(True) 
        self.Logout.clicked.connect(self.close_application)
        self.continueShopping.clicked.connect(self.continue1)
        
    def continue1(self):
        self.hide()
            
    def close_application(self):
            reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit the application?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                QCoreApplication.quit()

