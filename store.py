from product import Product
from customer import Customer
from shippingmethod import ShippingMethod

class Store(object):

    def __init__(self):
        self.__customers = []
        self.__products = []
        self.read_products('inventory.txt')
        self.__shippingMethods = []
        self.read_shipping_methods('shipping.txt')

    def __str__(self):
        string = 'products:'
        if self.__products == []:
            string += '\n   none'
        else:
            for product in self.__products:
               string += f'\n   {product}'
        string += '\nshipping methods:'
        if self.__shippingMethods == []:
            string += '\n   none'
        else:
            for method in self.__shippingMethods:
               string += f'\n   {method}'
        string += '\ncustomers:'
        if self.__customers == []:
            string += '\n   none'
        else:
            for customer in self.__customers:
                string += f'\n   {customer.name}'
        return string

    def read_products(self, filename):
        """Read the available products from a file."""
        with open(filename, 'r') as productsFile:
            for line in productsFile:
                name, type, price = line.split(',')
                try:
                    self.__products.append(Product(name, type, price))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_shipping_methods(self, filename):
        """Read the available products from a file."""
        with open(filename, 'r') as shippingFile:
            for line in shippingFile:
                name, description, basePrice, pricePerPound = line.split(',')
                try:
                    self.__shippingMethods.append(ShippingMethod(name, description, basePrice, pricePerPound))
                except TypeError:
                    print(f'{name} not added to shipping methods. Check {filename}.')

    def sales(self):
        """Returns the total dollar amount sold today."""
        pass

    def shipping(self):
        """Returns the total shipping amount today."""
        pass

    def tax(self):
        """Returns the total tax collected today."""
        pass

    def add_customer(self, customer):
        self.__customers.append(customer)
