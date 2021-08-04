
class Vendor:

    def __init__(self,vid,vnm,adr):
        self.vendorRegNo=vid
        self.vendorName=vnm
        self.vendorAddress=adr
        self.vendorProducts=[]

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


