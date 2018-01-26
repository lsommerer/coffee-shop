from toolbox import is_number
from store import Store
from customer import Customer
from product import Product
from order import Order
from address import Address
from lineitem import LineItem
from shippingmethod import ShippingMethod

def test():
    print('\n----product test----')
    product = Product('Bubble Tea', 'tea', 13.50)
    print(product)

    print('\n----shipping method test----')
    shippingMethod = ShippingMethod('FedEX', 'Faster and more expensive', 0.00, 4.65)
    print(shippingMethod)

    print('\n----address test----')
    address = Address('1100 North 56th Street', 'Lincoln', 'NE', '68434')
    print(address)

    print('\n----line item test----')
    lineItem = LineItem(product, 3.5)
    print(lineItem)

    print('\n----order test 1----')
    order = Order(shippingMethod, address)
    print(order)
    order.add(product, 3.5)
    order.add(product, 1)
    print('\n----order test 2----')
    print(order)

    print('\n----customer test 1----')
    name = 'Lloyd Sommerer'
    customer = Customer(name, address)
    print(customer)
    customer.add(order)
    print('\n----customer test 2----')
    print(customer)
    
    print('\n----store test 1----')
    store = Store()
    print(store)
    store.add_customer(customer)
    print('\n----store test 2----')
    print(store)

test()
