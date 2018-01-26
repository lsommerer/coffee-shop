from toolbox import is_number

class ShippingMethod(object):

    def __init__(self, name, description, basePrice, pricePerPound):
        self.__name = str(name).strip()
        self.__description = str(description).strip()
        if is_number(basePrice):
            self.__basePrice = float(basePrice)
        else:
            raise TypeError('ShippingMethod basePrice must be a numerical type.')
        if is_number(pricePerPound):
            self.__pricePerPound = float(pricePerPound)
        else:
            raise TypeError('ShippingMethod pricePerPound must be a numerical type.')

    def __str__(self):
        string =  f'{self.name} ${self.__basePrice:0.2f} + ${self.__pricePerPound:0.2f}/lb '
        string += f'({self.description})'
        return string
    
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_base_price(self):
        return self.__basePrice

    def get_price_per_pound(self):
        return self.__pricePerPound

    name = property(get_name)
    description = property(get_description)
    basePrice = property(get_base_price)
    pricePerPound = property(get_price_per_pound)
 
