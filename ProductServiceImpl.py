from oop_impl.ProductServiceInfo import VendorService
from oop_impl.ProductDAOImpl import VendorDAOImpl
from oop_impl.ProductInfo import Product
class VendorServiceImpl(VendorService): #how

    dao=None
    def __init__(self):
        VendorServiceImpl.dao=VendorDAOImpl()


    def add_product(self,uprodlist):

        if type(uprodlist)==list:
            for uprod in uprodlist:
                self.product_add(uprod)
        else:
            self.product_add(uprodlist)




    def product_add(self,uprod):
        if type(uprod) == Product:
            if uprod.productId > 0:
                if uprod.productPrice > 500:
                    if uprod.productQuantity > 0:
                        if self.get_product(uprod.productId):
                            print('Duplicate Product...cannt save it again')
                        else:
                            VendorServiceImpl.dao.insert_product(uprod)
                            print("Product saved Successfully....")
                    else:
                        print('Invalid product Quantity')
                else:
                    print('Invalid product price...')
            else:
                print('Invalid Product Id')
        else:
            print('INvalid product type..cannot save..!')

    def get_product(self,pid):
        if pid>0:
            row=VendorServiceImpl.dao.fetch_product(pid)
            return self.convert_rows_to_products(row)
        else:
            print('INvalid product id..')

    def get_all_products(self):
        rows = VendorServiceImpl.dao.fetch_all_products()
        return self.convert_rows_to_products(rows)

    def update_product(self,uprod):
        pass

    def remove_product(self,pid):
        if pid>0:
            if self.get_product(pid):
                rows = VendorServiceImpl.dao.delete_product(pid)
                return self.convert_rows_to_products(rows)
            else:
                print("product not present..so cannot delete")
        else:
            print('INvalid product Id')


    def convert_rows_to_products(self,rows):#() ((),())
        listOfProducts = []
        if rows :
            print(type(rows[0]))
            if type(rows[0])==tuple:
                for row in rows:
                   listOfProducts.append(Product(pid=row[0], pnm=row[1], pprice=row[2], pqty=row[3], pcat=row[4]))
                return listOfProducts
            else:
                return Product(pid=rows[0], pnm=rows[1], pprice=rows[2], pqty=rows[3], pcat=rows[4])
        else:
            print('No records exists..')