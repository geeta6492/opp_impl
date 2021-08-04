

class Address:

    def __init__(self,aid,city,state,pincode):
        self.addressId=aid
        self.addressCity=city
        self.addressState=state
        self.addressPincode=pincode

    def __str__(self):
        return f'\n{self.__dict__}'


    def __repr__(self):
        return str(self)

