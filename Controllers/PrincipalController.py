import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.Product import Product

class PrincipalController():

    def __init__(self, principal):
        self.product = Product(connection())
        self.principal = principal
    
    def listProducts(self):
        table = self.principal.table_product
        products = self.product.getProducts()
        table.setRowCount(0)
        for row_number, row_data in enumerate(products):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def showProduct(self):
        table = self.principal.table_product
        if table.currentItem() != None:
            cod = table.currentItem().text()
            print(cod)
            product = self.product.getProduct(cod)
            if product:
                print(product)
                msg = QMessageBox()
                msg.setWindowTitle(product[1])
                msg.setText(product[1])

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText('Codigo: '+product[0]+'\nNombre: '+product[1]+'\nPrecio: '+product[2]+'\nCategoria: '+product[3])

                x = msg.exec_()
    
    def updateProducs(self):
        table = self.principal.table_product
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                products.append(fila)
            fila = []
        
        if len(products)>0:
            for prod in products:
                self.product.updateProduct(prod[0],prod[1],prod[2],prod[3])
        
        self.listProducts()
    
    def deleteProduct(self):
        table = self.principal.table_product
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.product.getProduct(cod)
            if product:
                self.product.deleteProduct(cod)
        self.listProducts()
    
    def openCreate(self, Ui_CreateProduct):
        self.principal.Form = QtWidgets.QWidget()
        self.principal.ui = Ui_CreateProduct()
        self.principal.ui.setupUi(self.principal.Form)
        self.principal.Form.show()