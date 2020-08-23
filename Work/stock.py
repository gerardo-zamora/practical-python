# stock.py
#
# Exercise 4.1

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, amount):
        self.shares -= amount
        
    def cost(self):
        print(self.shares * self.price)
