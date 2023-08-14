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

        '''
        self._validate_width()
        self._validate_height()
        self._validate_x()
        self._validate_y()
        '''

        @property
        def width(self):
            '''Get the width'''
            return self.__width
        
        @width.setter
        def width(self, new_width):
            '''Set the width and validates'''
            if type(new_width) is not int:
                raise TypeError("width must be an integer")
            if new_width <= 0:
                raise ValueError("Width must be > 0")
            self.__width = new_width

        @property
        def height(self):
            '''Get the height'''
            return self.__height
        
        @height.setter
        def height(self, new_height):
            '''Set the height and validates'''
            if type(new_height) is not int:
                raise TypeError("Height must be an integer")
            if new_height <= 0:
                raise ValueError("Height must be > 0")
            self.__height = new_height
        
        @property
        def x(self):
            '''Get the x position'''
            return self.__x
        
        @x.setter
        def x(self, new_x):
            '''Set the x position and validates.'''
            if type(new_x) is not int:
                raise TypeError("x must be an integer")
            if new_x < 0:
                raise ValueError("x must be >= 0")
            self.__x = new_x
        
        @property
        def y(self):
            '''Get the y position'''
            return self.__y
        
        @y.setter
        def y(self, new_y):
            '''Set the y position and validates'''
            if type(new_y) is not int:
                raise TypeError("y must be an integer")
            if new_y < 0:
                raise ValueError("y must be >= 0")
            self.__y = new_y

        '''
        def _validate_width(self):
            """Validate the width attribute."""
            if not isinstance(self.__width, int):
                raise TypeError("width must be an integer")
            if self.__width <= 0:
                raise ValueError("width must be > 0")
            
        def _validate_height(self):
            """Validate the height attribute."""
            if not isinstance(self.__height, int):
                raise TypeError("height must be an integer")
            if self.__height <= 0:
                raise ValueError("height must be > 0")
            
        def _validate_x(self):
            """Validate the x attribute."""
            if not isinstance(self.__x, int):
                raise TypeError("x must be an integer")
            if self.__x < 0:
                raise ValueError("x must be >= 0")
            
        def _validate_y(self):
            """Validate the y attribute."""
            if not isinstance(self.__y, int):
                raise TypeError("y must be an integer")
            if self.__y < 0:
                raise ValueError("y must be >= 0")
        '''
        def area(self):
            '''area method: returns width * height'''
            return self.__width * self.__height
        
        def display(self):
            '''Display the rectangle using char #.'''
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

        def __str__(self):
            '''
            overrides __str__
            Returns:
                formatted string of rectangle attributes
            '''
            return ("[Rectangle] ({}) {}/{} - {}/{}").format(self.id, self.__x, self.__y, self.__width, self.__height) 
        
        def update(self, *args, **kwargs):
            """Update attributes using *args."""
            if args and len(args) > 0:
                self.id = args[0]
            if args and len(args) > 1:
                self.width = args[1]
            if args and len(args) > 2:
                self.height = args[2]
            if args and len(args) > 3:
                self.x = args[3]
            if args and len(args) > 4:
                self.y = args[4]

            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value