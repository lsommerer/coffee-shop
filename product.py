from toolbox import is_number

class Product(object):

    def __init__(self, name, type, price):
        self.__name = str(name).strip()
        if is_number(price):
            self.__price = float(price)
        else:
            raise TypeError('Product price must be a numerical type.')
        type = str(type).strip()
        if type in ['coffee', 'tea']:
            self.__type = type
        else:
            raise TypeError('Product type must be coffee or tea.')
    def __str__(self):
        return f'{self.name} ({self.type}) ${self.price:0.2f}/lb'

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__price

    name = property(get_name)
    type = property(get_type)
    price = property(get_price)
