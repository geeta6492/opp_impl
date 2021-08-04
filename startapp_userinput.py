from oop_impl.ProductInfo import Product
from oop_impl.ProductServiceImpl import VendorServiceImpl

service = VendorServiceImpl()

def add_product():
    pid = int(input('Enter Product Id : '))
    pname = input('Enter Product Name : ')
    pprice = float(input('Enter Product Price : '))
    pcat = input('Enter Product Category: ')
    pqt = int(input('Enter Product Qty : '))

    newprod = Product(pid=pid, pnm=pname, pprice=pprice, pcat=pcat, pqty=pqt)
    service.add_product(newprod)

def get_product():
    pid = int(input('Enter Product Id to fetch the data : '))
    prod = service.get_product(pid)
    print(prod)

def delete_product():

    prods = service.get_all_products()
    print('Existing products : ',prods)


    pid = int(input('Enter Product Id to delete the data : '))

    products = service.remove_product(pid)
    print("Latest Products",products)

def update_product():
    pid = int(input('Enter Product Id : '))
    if service.get_product(pid):
        pname = input('Enter Product Name : ')
        pprice = float(input('Enter Product Price : '))
        pcat = input('Enter Product Category: ')
        pqt = int(input('Enter Product Qty : '))
        newprod = Product(pid=pid, pnm=pname, pprice=pprice, pcat=pcat, pqty=pqt)
        service.update_product(newprod)
    else:
        print('given product id doesnt match with database..try again...')


def get_all_products():
    products = service.get_all_products()
    print(products)

def application_start(user_choice):

    service_choice = {
        1: add_product,
        2: get_product,
        3: delete_product,
        4: update_product,
        5: get_all_products,
    }
    return service_choice.get(user_choice)


if __name__ == '__main__':

    while True:
        SERVICE_CHOICE = '''
        1. ADD PRODUCT
        2. GET PRODUCT
        3. DELETE PRODUCT
        4. UPDATE PRODUCT
        5. GET ALL PRODUCT
        '''

        print(SERVICE_CHOICE)

        choice = int(input('Your Choice : '))
        op = application_start(choice)

        if op:
            op()
        else:
            print('Invalid Choice...!')

        ch = input('Do you want to continue....!')
        if ch=='No':
            break