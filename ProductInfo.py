

class Product:

    def __init__(self,pid,pnm,pprice,pcat,pqty):
        self.productId = int(pid)
        self.productName=str(pnm)
        self.productPrice=float(pprice)
        self.productCategory=str(pcat)
        self.productQuantity=int(pqty)

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


