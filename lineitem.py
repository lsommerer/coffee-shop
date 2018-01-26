class LineItem(object):

    def __init__(self, product, amount):
        self.product = product
        if amount > 0:
            self.amount = amount
        else:
            raise ValueError('Amount must be greater than zero.')
        self.total = product.price * amount
        
    def __str__(self):
        return f'{self.product.name:30s} ${self.product.price:0.2f}/lb   x {self.amount:5.0f} lbs    =    ${self.total:0.2f}'

