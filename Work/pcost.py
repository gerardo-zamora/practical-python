# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    '''Calculates portfolio cost on a CSV formated file for share name, number of shares, price per share'''
    
    portfolio = report.read_portfolio('Data/portfolio.csv')
    return portfolio.total_cost
    
def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
        
    cost = portfolio_cost(filename)
    print(f'Total cost: ${cost}')

if __name__ == '__main__':
    main(sys.argv)
