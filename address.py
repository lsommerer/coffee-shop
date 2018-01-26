class Address(object):

    taxes = {"AL":4, "AK":0, "AZ":5.6, "AR":6.5, "CA":7.25, "CO":2.9, "CT":6.35, "DC":5.75, "DE":0, "FL":6, "GA":4,
          "HI":4, "ID":6, "IL":6.25, "IN":7, "IA":6, "KS":6.5, "KY":6, "LA":5, "ME":5.5, "MD":6,
          "MA":6.25, "MI":6, "MN":6.875, "MS":7, "MO":4.225, "MT":0, "NE":5, "NV":6.85, "NH":0, "NJ":6.875,
          "NM":5.125, "NY":4, "NC":4.75, "ND":5, "OH":5.75, "OK":4.5, "OR":0, "PA":6, "RI":7, "SC":6,
          "SD":4.5, "TN":7, "TX":6.25, "UT":5.95, "VT":0, "VA":5.3, "WA":6.5, "WV":6, "WI":5, "WY":4}

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

    def get_tax_rate(self):
        return Address.taxes[self.state] / 100

    tax_rate = property(get_tax_rate)


