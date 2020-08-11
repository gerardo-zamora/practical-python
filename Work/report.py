# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Reads portafolio file and returns a list of dictionaries'''
    portfolio = []
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for rown, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError:
                print(f'Could not read row {rown}:', row)
        
    return portfolio
    
def read_prices(filename):
    '''Reads stock prices from file and returns a dictionary keyed by stock name'''
    prices = {}
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for rown, row in enumerate(rows, start=1):
            if len(row) == 2:
                try:
                    prices[row[0]] = float(row[1])
                except ValueError:
                    print('Could not read row:', row)
            else:
                print('Row', rown, 'has missing data or is empty')
    return prices
    
def make_report(portfolio, prices):
    '''Returns a report based on changes to a portfolio given current stock prices'''
    total_cost = 0.0
    total_value = 0.0
    report = []
    
    for stock in portfolio:
        change = prices[stock['name']] - stock['price']
        report.append((stock['name'], stock['shares'], prices[stock['name']], change))
    
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

portfolio_report('Data/portfoliodate.csv','Data/prices.csv')

