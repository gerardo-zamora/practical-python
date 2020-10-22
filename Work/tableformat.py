# tableformat.py
#
# Exercise 4.5

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
        
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format.
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
class CSVTableFormatter(TableFormatter):
    '''
    Emit a table in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))
        
class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
        
class FormatError(Exception):
    pass

def create_formatter(format):
    '''
    Create a formatter using the given format.
    '''
    if format == 'txt':
        formatter = TextTableFormatter()
    elif format == 'csv':
        formatter = CSVTableFormatter()
    elif format == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {format}')
    
    return formatter

def print_table(data, attributes, formatter):
    '''
    Print a table with the given arbitrary data and user-specified attributes.
    '''
    # Print headers (user-specified attributes)
    formatter.headings(attributes)
    
    # Print data columns
    for row in data:
        attr_data = [ str(getattr(row, attr)) for attr in attributes ]
        formatter.row(attr_data)

            
        
        
