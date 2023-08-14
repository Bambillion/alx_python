'''
This Module defines the Rectangle class.
'''
from models.base import Base

class Rectangle(Base):
    '''
    A rectangle class.
    
    Attributes:
        width(int): The width
        height(int): The height
        x(int): The x position
        y(int): The y position
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initilaize the rectangle instance with specified attributes.
        
        Args:
            width(int): The width
            height(int): The height
            x(int, optional): The x position Default is  0.
            y(int, optional): The y position Default is 0.
            id(int, optional): The identifier inherits from the Base class.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            '''Get the width'''
            return self.__width
        
        @property
        def height(self):
            '''Get the height'''
            return self._height
        
        @property
        def x(self):
            '''Get the x position'''
            return self._x
        
        @property
        def y(self):
            '''Get the y position'''
            return self._y