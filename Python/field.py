class ShoppingCart:
    prices = []
 
    def __init__(self):
        self.prices = []

    '''
    the goal is to remove the field above, using a list of prices instead:
    def __init__(self):
        self.prices = []
    '''

    def add(self, price):
        self.prices.append(price)
        
    def calculate_total_price(self):
        return sum(self.prices)

    def has_discount(self):
        return self.calculate_total_price() >= 100

    def number_of_products_new(self):
        return len(self.prices)


class SomeConsumer():
    def do_stuff(self):
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products_new())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
