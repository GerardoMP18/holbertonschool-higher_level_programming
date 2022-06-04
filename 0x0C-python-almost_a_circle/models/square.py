#!/usr/bin/python3
"""
- And now, the Square
- Square update
- Square instance to dictionary representation
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Create class Square with inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """
    Method that allows us to perform the update assigned to us
    the argument of each attribute and keywords
    """
    def update(self, *args, **kwargs):
        numArgs = len(args)
        arguments = ['id', 'size', 'x', 'y']
        if (numArgs != 0 and args is not None):
            for index in range(numArgs):
                setattr(self, arguments[index], args[index])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """
    Representation of dictionary of a square
    """
    def to_dictionary(self):
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
