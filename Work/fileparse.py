# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None, verbose=True):
    '''
    Parse a CSV file into a list of records
    '''
    
    if select and has_headers == False:
        raise RuntimeError("Argument 'select' requires column headers")
    
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)
        
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
