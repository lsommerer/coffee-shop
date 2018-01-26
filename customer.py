class Customer(object):

    def __init__(self, name = None, address = None):
        self.name = name
        self.address = address
        self.__orders = []

    def add(self, order):
        self.__orders.append(order)

    def __str__(self):    
        string = f'{self.name}\n{self.address}\n\nOrders for {self.name}:'
        if self.__orders == []:
            string += '\n   none'
        else:
            for order in self.__orders:
                string += f'\n{order}'
        return string

    def mailing_label(self):
        return f'{self.name}\n{self.address}'
    
