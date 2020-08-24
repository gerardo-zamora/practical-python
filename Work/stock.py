# stock.py
#
# Exercise 4.1

class Stock:
    '''
    Instance of a stock holding containing name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, amount):
    '''
    Sell amount of shares.
    '''
        self.shares -= amount
        
    def cost(self):
    '''
    Returns the cost of a stock holding.
    '''
        return self.shares * self.price
