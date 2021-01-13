# ticker.py
#

import csv
import report
import tableformat
from follow import follow

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
        
def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def select_columns(rows, indeces):
    for row in rows:
        yield [row[index] for index in indeces]
    

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines, select, headers, types):
    rows = csv.reader(lines)
    rows = select_columns(rows, select)
    rows = convert_types(rows, types)
    rows = make_dicts(rows, headers)
    return rows

def ticker(portfile, logfile, format):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    formatter = tableformat.create_formatter(format)
    headings = ['name', 'price', 'change']
    rows = parse_stock_data(lines,
                            [0, 1, 4],
                            headings,
                            [str, float, float])
    #rows = filter_symbols(rows, portfolio)
    rows = (row for row in rows if row['name'] in portfolio)
    
    formatter.headings(headings)
    
    for row in rows:
        formatter.row([row['name'], f'${row["price"]:0.2f}', f'{row["change"]:0.2f}'])
        
if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')

