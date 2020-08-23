# report.py
#
# Exercise 2.4
import csv
import sys
import fileparse
from stock import Stock

def read_portfolio(filename):
    '''Reads portafolio file and returns a list of dictionaries'''
    portdicts = []
    
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file, select=['name','shares','price'], types=[str,int,float])
    
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    
    return portfolio
    
def read_prices(filename):
    '''Reads stock prices from file and returns a dictionary keyed by stock name'''
    with open(filename) as file:
        pricelist = fileparse.parse_csv(file, types=[str,float], has_headers=False)
        prices = { name : price for name,price in pricelist }
    
    return prices
    
def make_report(portfolio, prices):
    '''Returns a report based on changes to a portfolio given current stock prices'''
    total_cost = 0.0
    total_value = 0.0
    report = []
    
    for s in portfolio:
        change = prices[s.name] - s.price
        report.append((s.name, s.shares, prices[s.name], change))
    
    return report
    
def print_report(report: list):
    '''
    Prints formatted report
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print((('-' * 10) + ' ') * len(headers))
    for name, shares, price, change in report:
        price_string = f'${price:0.2f}'
        price_string = ' ' * (10-len(price_string)) + price_string
        print(f'{name:>10s} {shares:>10d} {price_string} {change:>10.2f}')
        
def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    # Set defaults
    portfolio_filename = 'Data/portfoliodate.csv'
    prices_filename = 'Data/prices.csv'
    
    if len(argv) == 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
        
    portfolio_report(portfolio_filename, prices_filename)
    
if __name__ == '__main__':
    main(sys.argv)

