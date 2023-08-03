'''
My Square Class
This module contains the square class.
This square class represents a square with a specified size. It has a private attribute __size
which stores the size of the square 

Attributes:
    __size(int): The size of the square.

Methods:
    __init__(self, size=0): Initialize a square object with an optional 
    size.
    area(self): Calculate and return the area of the square.
    
Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
'''

class Square:
    '''
    A class that represents a square.
    
    Attributes:
    __size(int): The size of the square.
    
    Methods:
        __init__(self, size): Initializes a square object with a given size
    '''
    def __init__(self, size=0):
        '''
        Initialize a square object.
        
        Args: 
            size(int): optional size of the square. default is 0.
            
        Raises: 
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size