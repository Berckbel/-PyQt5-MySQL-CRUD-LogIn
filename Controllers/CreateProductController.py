import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Product import Product

class CreateProductController():
    def __init__(self, create_product):
        self.product = Product(connection())
        self.create_product = create_product
    
    def createProduct(self,cod,name,price,category, CreateProduct):
        if cod and name and price and category:
            self.product.insertProduct(cod,name,price,category)
            CreateProduct.hide()