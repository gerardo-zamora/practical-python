# stock.py
#
# Exercise 4.1

class Stock:
    '''
    Instance of a stock holding containing name, shares, and price.
    '''
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    # Used with `repr()`
    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
        
    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
        
    @property
    def cost(self):
        '''
        Returns the cost of a stock holding.
        '''
        return self.shares * self.price
    
    # Used with `str()`
    def str(self):
        return f'{self.name},{self.shares},{self.price}'

    def sell(self, amount):
        '''
        Sell amount of shares.
        '''
        self.shares -= amount
