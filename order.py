from lineitem import LineItem

class Order(object):

    def __init__(self, shippingMethod = None, address = None):
        self.__address = address
        self.__shippingMethod = shippingMethod
        self.__lineItems = []

    def __str__(self):
        string = f'address: \n{self.__address} \n\nshipping: \n{self.__shippingMethod}\n\n'
        string += '    Item                              Cost        Quantity         Total\n'
        string += '-------------------------------------------------------------------------'
        if self.__lineItems == []:
            string += '\n   none'
        else:
            for line in self.__lineItems:
                string += f'\n   {line}'
        return string
    
    def add(self, product, amount):
        newLine = LineItem(product, amount)
        self.__lineItems.append(newLine)

    def get_tax(self):
        pass

    def get_shipping(self):
        pass

    def get_sales(self):
        pass

    def get_total(self):
        pass
