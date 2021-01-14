# stock.py
#
# Exercise 7.7

from typedproperty import typedproperty, String, Integer, Float

class Stock:
    '''
    Instance of a stock holding containing name, shares, and price.
    '''
    __slots__ = ('name', '_shares', 'price')
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    # Used with `repr()`
    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
        
    @property
    def cost(self):
        '''
        Returns the cost of a stock holding.
        '''
        return self.shares * self.price

    def sell(self, amount):
        '''
        Sell amount of shares.
        '''
        self.shares -= amount
