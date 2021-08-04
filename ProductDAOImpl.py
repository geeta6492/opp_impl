
from oop_impl.ProductDAOInfo import VendorDAO
from oop_impl.dbconfig import get_database_connection

class VendorDAOImpl(VendorDAO):
    conn=None

    def __init__(self):
        VendorDAOImpl.conn=get_database_connection()
        #self.create_product_table()

    def create_product_table(self):
        PRODUCT_CREATE_TABLE_SQL='''
            CREATE TABLE IF NOT EXISTS product_info (
                product_id INT AUTO_INCREMENT,
                product_name VARCHAR(255) NOT NULL,
                product_price FLOAT NOT NULL,
                product_qty INT NOT NULL,
                product_cat VARCHAR(255) NOT NULL,
                PRIMARY KEY (product_id)
                )
            '''
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(PRODUCT_CREATE_TABLE_SQL)
        VendorDAOImpl.conn.commit()

    def insert_product(self, pr):
        SQL = "INSERT INTO PRODUCT_INFO VALUES("
        SQL += str(pr.productId) + ",'" + pr.productName + "'," + str(pr.productPrice) + "," + str(
            pr.productQuantity) + ",'" + pr.productCategory + "'" + ")"

        cursor =VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()

    def fetch_product(self, pid):
        SQL = "SELECT * FROM PRODUCT_INFO WHERE PRODUCT_ID="+str(pid)
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        return cursor.fetchone()

    def fetch_all_products(self):
        SQL = "SELECT * FROM PRODUCT_INFO"
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        return cursor.fetchall()


    def modify_product(self, uprod):
        pass

    def delete_product(self, pid):
        SQL = "DELETE FROM PRODUCT_INFO WHERE PRODUCT_ID="+str(pid)
        cursor = VendorDAOImpl.conn.cursor()
        cursor.execute(SQL)
        VendorDAOImpl.conn.commit()

        return self.fetch_all_products()
