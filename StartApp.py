from oop_impl.ProductInfo import Product
from oop_impl.ProductServiceImpl import VendorServiceImpl
if __name__ == '__main__':
    #pr1 = Product(pid=102,pnm="AAA",pprice=8322.3,pcat="A",pqty=10)
    pr2 = Product(pid=1022, pnm="AAA", pprice=8322.3, pcat="A", pqty=10)
    #pr3 = Product(pid=102, pnm="AAA", pprice=8322.3, pcat="A", pqty=10)

    vendorServices = VendorServiceImpl()
    vendorServices.add_product(pr2)

    '''
    adrr = Address(aid=1122,city="Pune",state="MH",pincode=234567)
    print(adrr)
    ven = Vendor(vid=9999,vnm="Flipkart",adr=adrr)
    print(ven)

    
    print(vendorServices) # serviceimpl
    print(vendorServices.dao) #daoimpl
    print(vendorServices.dao.conn) #connection
    '''