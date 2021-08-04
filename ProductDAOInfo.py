from abc import ABC,abstractmethod


class VendorDAO(ABC):

    @abstractmethod
    def insert_product(self,uprod):
        pass

    @abstractmethod
    def fetch_product(self,pid):
        pass

    @abstractmethod
    def fetch_all_products(self):
        pass

    @abstractmethod
    def modify_product(self,uprod):
        pass

    @abstractmethod
    def delete_product(self,pid):
        pass