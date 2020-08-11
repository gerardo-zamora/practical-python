# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):
    '''Calculates portfolio cost on a CSV formated file for share name, number of shares, price per share'''
    
    total_cost = 0.0
    
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows) # process headers first
        for rown, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                total_cost = total_cost + (int(record['shares']) * float(record['price']))
            except ValueError:
                print(f'Could not parse row {rown}:', row)

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: ${cost}')
