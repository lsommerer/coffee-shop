class LineItem(object):

    def __init__(self, product, amount):
        self.__product = product
        if amount > 0:
            self.__amount = amount
        else:
            raise ValueError('Amount must be greater than zero.')
        self.__total = product.price * amount
        
    def __str__(self):
        return f'{self.product.name:30s} ${self.product.price:0.2f}/lb   x {self.amount:5.2f} lbs    =    ${self.total:7.2f}'

    def get_product(self):
        return self.__product

    def get_amount(self):
        return self.__amount

    def get_total(self):
        return self.__total

    product = property(get_product)
    amount = property(get_amount)
    total = property(get_total)
