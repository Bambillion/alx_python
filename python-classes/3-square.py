'''
My square Class

This module defines a simple square class to represent squares in a two-dimensional space. The square class
has an attribute "size" to store the size of the squrae. The size is a positive integer that represents the
length of each side of the square.

Attributes:
    size(int): The size of the square, i.e., the length of each side.
    
Methods:
    __init__(self, size): Constructor method to initialize the square object with a given size.
    
Example:
    # >>> square1 = Square(5)
Note:
    This implementation of the square class doesn't perform type or value validation on the "size" attribute
    It is assumed taht the sise attribute will always be a positive integer.
'''
class Square:
    '''
    This class represents a Square object.
    
    Attributes:
        __size(int): The size of the square
        
    Methods:
        __init__(self, size=0): Initialize a square object with an optional size.
        area(self): Calculate and return the area of a square
    
    Properties:
        size(int): Getter and setter for the size of teh square.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    '''
    def __init__(self, size=0):
        '''
        Initialize a Square object.
        Args:
            size(int): optional size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0
        '''
        self.size = size

    @property
    def size(self):
        '''
        Get the size of the square.
        Returns:
            int: The size of the square.
        '''
        return self.__size
        
    @size.setter
    def size(self, value):
        '''
        Set the size of the square
        Args:
            value(int): The new size of the square.        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        '''
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2