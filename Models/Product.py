class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS product
                        (cod VARCHAR(45) NOT NULL,
                        name VARCHAR(45) NOT NULL,
                        price VARCHAR(45) NOT NULL,
                        category VARCHAR(45) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()
    
    def getProducts(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getProduct(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product WHERE cod = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateProduct(self,cod,name,price,category):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET name = %s, price = %s, category = %s WHERE cod = %s """
            cursor.execute(sql,(name,price,category,cod))
            self.conn.commit()

    def deleteProduct(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM product WHERE cod = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertProduct(self,cod,name,price,category):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO product (cod,name,price,category) VALUES (%s,%s,%s,%s)"""
            cursor.execute(sql, (cod,name,price,category))
            self.conn.commit()