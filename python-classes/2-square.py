#!/usr/bin/python3
'''
My Square Class
This module defines a simple Square class to represent squares in a two-dimensional space.
The square class has an attribute "size" to store the size of the square. The size is a positive 
integer that represensts the length of each side of the square.

Attributes:
    size(int): The size of the square, i.e the length of each side.

Methods:
    __init__(self, size): Constructor method to initialize the square object with a given size

Example:
    # >>> square1 = square(5)

Note: 
    This  implementation of the square classdoes not perform type or value validation on the "size" attribute.
    It is assumed that the "size" attribute will always be a positive integer.
'''
class Square:
    '''
    This class represents a square object.
    
    Attributes:
        __size(int): The size of the square.
        
    Methods:
        __init__(self, size=0): Initialize a square object with an optional size.
        area(self): Calculate and return the area of the square.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    '''
    def __init__(self, size=0):
        '''
        Initialize a square object.
        
        Args:
            size(int): Optional size of the square. Default is 0
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate and return the area of the square.
        
        Returns:
            int: The area of the square
        '''
        return self.__size ** 2

