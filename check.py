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


    def SearchMaterial(self):
        criteria = self.searchMaterialCriteria.currentText().strip()
        criteriaValue = self.searchMaterialValue.text().strip()

        if (criteria != '' and criteriaValue != ''):        
            # print('criteria: ', criteria)

            if criteria == 'Material Name':
                sql_query = 'select * from Material where materialName like (?)'
                cursor.execute(sql_query, ('%' + criteriaValue + '%',))
                #connection.commit()
                self.materialTable.clearContents()
                self.materialTable.setRowCount(0)

                rows = cursor.fetchall()

                if not rows:
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setWindowTitle("No Results")
                    self.msg.setText("No results found for the given search criteria.")
                    self.msg.show()
                    self.PopulateMaterialTable()
                    return

                for row_index, row_data in enumerate(cursor.fetchall()):
                    print('populating row')
                    self.materialTable.insertRow(row_index)
                    for col_index, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        print('Adding item to material table.')
                        self.materialTable.setItem(row_index, col_index, item)

            elif criteria == 'Description':
                sql_query = 'select * from Material where description like (?)'
                cursor.execute(sql_query, ('%' + criteriaValue + '%',))
                #connection.commit()     
                self.materialTable.clearContents()
                self.materialTable.setRowCount(0)

                rows = cursor.fetchall()

                if not rows:
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setWindowTitle("No Results")
                    self.msg.setText("No results found for the given search criteria.")
                    self.msg.show()
                    self.PopulateMaterialTable()
                    return

                for row_index, row_data in enumerate(cursor.fetchall()):
                    print('populating row')
                    self.materialTable.insertRow(row_index)
                    for col_index, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        print('Adding item to material table.')
                        self.materialTable.setItem(row_index, col_index, item)

            elif criteria == 'Units':
                if criteriaValue.isdigit():
                    sql_query = 'select * from Material where units = (?)'
                    cursor.execute(sql_query, (criteriaValue,))

                    self.materialTable.clearContents()
                    self.materialTable.setRowCount(0)

                    rows = cursor.fetchall()

                    if not rows:
                        self.msg = QtWidgets.QMessageBox()
                        self.msg.setWindowTitle("No Results")
                        self.msg.setText("No results found for the given search criteria.")
                        self.msg.show()
                        self.PopulateMaterialTable()
                        return

                    for row_index, row_data in enumerate(cursor.fetchall()):
                        print('populating row')
                        self.materialTable.insertRow(row_index)
                        for col_index, cell_data in enumerate(row_data):
                            item = QTableWidgetItem(str(cell_data))
                            print('Adding item to material table.')
                            self.materialTable.setItem(row_index, col_index, item)

                else:
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setWindowTitle('Error')
                    self.msg.setText('Units should be a numeric value')
                    self.msg.show()            

            print('Query executed')
            
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle('Error')
            self.msg.setText('Please select search criteria and/or enter search value')
            self.msg.show()