# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', verbose=True):
    '''
    Parse a CSV file into a list of records
    '''
    
    if isinstance(lines, str):
        raise ValueError("File-like or iterable object expected! Did you input a path?")
    
    if select and has_headers == False:
        raise RuntimeError("Argument 'select' requires column headers")
    
    rows = csv.reader(lines, delimiter=delimiter)
    
    if has_headers:
        # Define headers
        headers = next(rows)
    else:
        headers = []
    
    # If select is provided, define indeces for the selected headers
    if select:
        indeces = [headers.index(col) for col in select]
        headers = select
    else:
        indeces = []
    
    # Init records variable to return
    records = []
    
    for rown, row in enumerate(rows, start=1):
        if not row:
            continue
        if indeces:
            row = [ row[index] for index in indeces ]
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError as reason:
                if verbose:
                    print('Row', rown, ':', 'Could not convert', row)
                    print('Row', rown, ':', 'Reason:', reason)
        if headers:
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)
    
    return records
