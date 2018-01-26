class Address(object):

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        if state in Address.states:
            self.state = state
        else:
            raise TypeError('Address requires a valid 2 letter US state postal code.')
        self.zipcode = zipcode

    def __str__(self):
        return f'{self.street}\n{self.city}, {self.state} {self.zipcode}'

