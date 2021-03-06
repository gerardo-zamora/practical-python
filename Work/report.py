# report.py
#
# Exercise 2.4
import csv
import sys
import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):
    '''Reads portafolio file and returns a list of dictionaries.'''
    portdicts = []
    
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)
    
    portfolio = [Stock(**d) for d in portdicts]
    
    return Portfolio(portfolio)
    
def read_prices(filename):
    '''Reads stock prices from file and returns a dictionary keyed by stock name.'''
    with open(filename) as file:
        pricelist = fileparse.parse_csv(file, types=[str,float], has_headers=False)
        prices = { name : price for name,price in pricelist }
    
    return prices
    
def make_report(portfolio, prices):
    '''Returns a report based on changes to a portfolio given current stock prices.'''
    total_cost = 0.0
    total_value = 0.0
    report = []
    
    for s in portfolio:
        change = prices[s.name] - s.price
        report.append((s.name, s.shares, prices[s.name], change))
    
    return report
    
def print_report(report, formatter):
    '''
    Prints formatted report.
    '''
    # Print headers
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    
    # Print rows
    for name, shares, price, change in report:
        formatter.row([name, str(shares), f'${price:0.2f}', f'{change:0.2f}'])
        
def portfolio_report(portfolio_filename, prices_filename, format='txt'):
    '''
    Creates and prints a report for the given stock portfolio file and given prices file.
    '''
    # Read data
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    # Create report
    report = make_report(portfolio, prices)
    
    # Print data
    formatter = tableformat.create_formatter(format)
    print_report(report, formatter)

def main(argv):
    # Set defaults
    portfolio_filename = 'Data/portfoliodate.csv'
    prices_filename = 'Data/prices.csv'
    
    # Determine if format was provided
    format_specified = len(argv) == 4
    
    if len(argv) >= 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
        if format_specified:
            format = argv[3]
            portfolio_report(portfolio_filename, prices_filename, format)
        else:
            portfolio_report(portfolio_filename, prices_filename)
    
if __name__ == '__main__':
    main(sys.argv)

