from lineitem import LineItem

class Order(object):

    def __init__(self, shippingMethod = None, address = None):
        self.__address = address
        self.__shippingMethod = shippingMethod
        self.__lineItems = []

    def __str__(self):
        string = f'address: \n{self.__address} \n\nshipping: \n{self.__shippingMethod}\n\n'
        string += '    Item                            Cost        Quantity             Total\n'
        string += '--------------------------------------------------------------------------'
        if self.__lineItems == []:
            string += '\n   none'
        else:
            for line in self.__lineItems:
                string += f'\n   {line}'
        string += '\n--------------------------------------------------------------------------\n'
        string += f'                                                {self.weight:5.2f} lbs         ${self.sales:7.2f}\n\n'
        string += f'                                                         taxes =  ${self.tax:7.2f}\n'
        string += f'                                                      shipping =  ${self.shippingCost:7.2f}\n'
        string += '                                                               ------------\n'
        string += f'                                                         total =  ${self.total:7.2f}\n'
        return string
    
    def add(self, product, amount):
        newLine = LineItem(product, amount)
        self.__lineItems.append(newLine)

    def get_weight(self):
        """Return the total weight of an order."""
        totalWeight = 0
        for item in self.__lineItems:
            totalWeight += item.amount
        return totalWeight

    def get_tax(self):
        return self.sales * self.__address.tax_rate

    def get_shipping_cost(self):
        return self.__shippingMethod.cost(self.weight)

    def get_sales(self):
        totalSales = 0
        for item in self.__lineItems:
            totalSales += item.total
        return totalSales

    def get_total(self):
        return self.sales + self.tax + self.shippingCost

    weight = property(get_weight)
    shippingCost = property(get_shipping_cost)
    sales = property(get_sales)
    tax = property(get_tax)
    total = property(get_total)