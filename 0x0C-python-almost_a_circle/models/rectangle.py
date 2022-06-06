#!/usr/bin/python3
"""
- First Rectangle
- Validate attributes
- Area first
- Display #0
- __str_i_
- Display #1
- Update #0
- Update #1
- Rectangle instance to dictionary representation
"""


from models.base import Base


class Rectangle(Base):
    """
    Create of constructor of class Rectangule with inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if(type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if(type(value) is not int):
            raise TypeError("height must be an integer")
        elif(value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif(value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Method that prints in stdout the rectangle instance
        with character #
        """
        for i in range(self.__y):
            print("\n", end="")
        for a in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Return message
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """
        Method that allows us to perform the update that assigns
        the argument to each attribute
        """
        numArgs = len(args)
        arguments = ['id', 'width', 'height', 'x', 'y']
        if (numArgs != 0 and args is not None):
            for index in range(numArgs):
                setattr(self, arguments[index], args[index])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Representation of dictionary of a rectangle
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x,
                'y': self.__y}
