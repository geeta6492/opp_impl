
from abc import ABC,abstractmethod

class VendorService(ABC):  #what

    @abstractmethod
    def add_product(self,uprod):
        pass

    @abstractmethod
    def get_product(self,pid):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def update_product(self,uprod):
        pass

    @abstractmethod
    def remove_product(self,pid):
        pass