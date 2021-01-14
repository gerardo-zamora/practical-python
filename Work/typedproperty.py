# typedproperty.py
#
# Exercise 7.7

class typedproperty(name, expected_type):
    '''
    Instance of a typed property that stores a value of expected_type.
    '''
    private_name = '_' + name
    
    def prop(self):
        return getattr(self, private_name)
        
    @prop.setter
    def prop(self, value):
        if not instance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)
    
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
