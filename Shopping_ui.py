# Form implementation generated from reading ui file 'd:\Third Semester files\database\project POSHAAK final\POSHAAK-database\Shopping.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(327, 10, 231, 26))
        self.label.setBaseSize(QtCore.QSize(12, 0))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.itemWidget.setGeometry(QtCore.QRect(20, 40, 771, 391))
        self.itemWidget.setObjectName("itemWidget")
        self.itemWidget.setColumnCount(8)
        self.itemWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemWidget.setHorizontalHeaderItem(7, item)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 520, 51, 20))
        self.label_4.setObjectName("label_4")
        self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.total.setGeometry(QtCore.QRect(320, 510, 121, 31))
        self.total.setObjectName("total")
        self.checkoutButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkoutButton.setGeometry(QtCore.QRect(620, 440, 121, 31))
        self.checkoutButton.setObjectName("checkoutButton")
        self.continueButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.continueButton.setGeometry(QtCore.QRect(620, 490, 121, 41))
        self.continueButton.setObjectName("continueButton")
        self.deleteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(200, 450, 101, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(80, 450, 91, 31))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "My Shopping Cart"))
        item = self.itemWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.itemWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.itemWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.itemWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        item = self.itemWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Size"))
        item = self.itemWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Color"))
        item = self.itemWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Price"))
        item = self.itemWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Discount(if any)"))
        self.label_4.setText(_translate("MainWindow", "Total"))
        self.checkoutButton.setText(_translate("MainWindow", "Checkout"))
        self.continueButton.setText(_translate("MainWindow", "Continue Shopping"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.backButton.setText(_translate("MainWindow", "Back"))
